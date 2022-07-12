"""Rank Documents with an lucnene index using Aserini"""
import collections
import itertools
import random
from typing import List
import time
import multiprocessing as mp

import numpy as np
import torch

from torch.utils.data import DataLoader, SequentialSampler

from bert.data_example import DataExample
#from logger import Logger
from bert.utils import Context, Answer, SquadResult

try:
    from transformers import BasicTokenizer, AutoModelForQuestionAnswering, \
        AutoTokenizer, squad_convert_examples_to_features
except ImportError:
    raise ImportError("""
    Bart will be released through pip in v 3.0.0, until then use it by installing from source:
        
    git clone git@github.com:huggingface/transformers.git
    git checkout d6de6423
    cd transformers
    pip install -e ".[dev]"
    """)


RawResult = collections.namedtuple("RawResult",
                                   ["unique_id", "start_logits", "end_logits"])


def to_list(tensor):
    return tensor.detach().cpu().tolist()


def set_seed(seed, n_gpu: int):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if n_gpu > 0:
        torch.cuda.manual_seed_all(seed)


class BertQA:

    def __init__(self, component_config: dict, **kwargs):
        self.component_config = component_config.get('BertReader')

        self.device = torch.device("cuda" if torch.cuda.is_available() and self.component_config.get('on_gpu')
                                   else "cpu") if not kwargs else kwargs.get('device')

        # load the BERT pre-trained model and tokenizer for QA
        self._model = AutoModelForQuestionAnswering.from_pretrained(self.component_config.get('model'), use_auth_token=True).to(self.device)
        self._tokenizer = AutoTokenizer.from_pretrained(self.component_config.get('tokenizer'),
                                                        use_fast=self.component_config.get('fast_tokenizer'))
        set_seed(self.component_config.get('seed'), self.component_config.get('n_gpu'))
        self._enable_n_best = self.component_config.get('enable_n_best')

    def predict(self, question: str, contexts: List[Context]) -> List[Answer]:
        print('question: {}'.format(question))
        print('contexts[0]: {}'.format(contexts[0].toJson()))
        examples = self.input_to_squad_examples(question, contexts)
        print('examples[0]: {}'.format(examples[0]))

        features, dataset = squad_convert_examples_to_features(
            examples=examples,
            tokenizer=self._tokenizer,
            max_seq_length=self.component_config.get('max_seq_length'),
            doc_stride=self.component_config.get('doc_stride'),
            max_query_length=self.component_config.get('max_query_length'),
            return_dataset="pt",
            threads=self.component_config.get("threads"),
            tqdm_enabled=self.component_config.get("tqdm_enabled"),
            is_training=False
        )

        # Note that DistributedSampler samples randomly
        eval_sampler = SequentialSampler(dataset)
        eval_dataloader = DataLoader(dataset, sampler=eval_sampler, batch_size=32)

        self._model.to(self.device)
        all_results = []
        for batch in eval_dataloader:
            self._model.eval()
            batch = tuple(t.to(self.device) for t in batch)
            with torch.no_grad():

                inputs = {
                    "input_ids": batch[0],
                    "attention_mask": batch[1],
                    "token_type_ids": batch[2],
                }

                feature_indices = batch[3]
                outputs = self._model(**inputs)

            for i, feature_index in enumerate(feature_indices):
                eval_feature = features[feature_index.item()]

                unique_id = int(eval_feature.unique_id)

                if self.component_config.get('on_gpu'):
                    output = [to_list(output[i]) for output in outputs.to_tuple()]
                else:
                    output = [output[i] for output in outputs.to_tuple()]

                start_logits, end_logits = output

                result = SquadResult(unique_id, start_logits, end_logits)

                all_results.append(result)

        print('_all_results: {size}'.format(size=len(all_results)))

        all_pred_answers, all_n_best = self.compute_predictions_logits(
            all_examples=examples,
            all_features=features,
            all_results=all_results,
            n_best_size=self.component_config.get("n_best_size"),
            max_answer_length=self.component_config.get("max_answer_length"),
            do_lower_case=self.component_config.get("do_lower_case"),
            version_2_with_negative=self.component_config.get("version_2_with_negative"),
            null_score_diff_threshold=self.component_config.get("null_score_diff_threshold"),
            tokenizer=self._tokenizer,
            enable_softmax=self.component_config.get("enable_softmax")
        )

        all_answers = []

        print('**---- all_nbest_json: {}'.format(all_n_best))
        print('**---- all_nbest_json size: {} -- {}'.format(len(all_n_best), len(list(all_n_best.values())[0])))
        print('**---- all_nbest_json size: {} -- {}'.format(len(all_n_best), len(list(all_n_best.values())[0])))
        print('**---- all_predictions size: {}'.format(len(all_answers)))

        self._model.to('cpu')
        if self._enable_n_best:
            # re-fomulate the n_best answer list
            n_bests = itertools.chain.from_iterable(list(all_n_best.values()))
            answers = {(ans.get('probability').item() if torch.is_tensor(ans.get('probability'))
                        else ans.get('probability')): dict(ans) for ans in n_bests}
            answers = collections.OrderedDict(sorted(answers.items(), reverse=True))

            has_first_empty_answer = False
            non_empty_answers = {}
            for prob, answer in answers.items():
                if has_first_empty_answer and not answer['text'].strip():
                    continue
                else:
                    if not answer['text'].strip():
                        has_first_empty_answer = True
                    non_empty_answers[prob] = answer

            answers = list(non_empty_answers.values())[:self.component_config.get("n_best_size")]

            end = time.time()
        else:
            answers = all_pred_answers.values()

        answer_inputs = [(ans, contexts, question) for ans in answers]
        if len(answer_inputs) > 10:
            answer_inputs = np.array_split(answer_inputs, 10)
        elif len(answer_inputs) > 5:
            answer_inputs = np.array_split(answer_inputs, 5)
        print('-- answer_inputs : {} - {}'.format(answer_inputs, len(answer_inputs)))

        all_final_answers = self.multi_process_answers(answer_inputs, contexts, question)

        _sorted_answers = dict(collections.OrderedDict(sorted(all_final_answers.items(), reverse=True)))
        _sorted_answers = list(_sorted_answers.values())

        _sorted_answers = [result.toJson() for result in _sorted_answers]
        print('_sorted_answers: {}'.format(_sorted_answers))
        end = time.time()
        self._model.to(self.device)
        return _sorted_answers

    def multi_process_answers(self, answer_inputs, contexts, question):
        with mp.Pool(len(answer_inputs)) as p:
            all_final_answers = p.map(self.prepare_answers, [answer_inputs, contexts, question])
            p.close()  # no more tasks
            p.join()  # wrap up current tasks
        all_final_answers = {k: v for answer in all_final_answers for k, v in answer.items()}
        return all_final_answers

    def process_answers(self, answer_inputs, contexts, question):
        all_final_answers = self.prepare_answers([answer_inputs, contexts, question])
        all_final_answers = {k: v for answer in all_final_answers for k, v in answer.items()}
        return all_final_answers

    @staticmethod
    def prepare_answers(args):
        answer_list = {}
        for item in args:
            print("item: {}".format(item))
            answer = item[0]
            contexts = item[1]
            question = item[2]

            _answer = Answer(text=answer['text'], score=answer['probability'],
                             query=question,
                             document=contexts[int(answer.get('doc_idx'))].toJson(),
                             document_id=answer.get('doc_idx'),
                             start_index=answer['start_index'], end_index=answer['end_index'])

            answer_list[_answer.score] = _answer
        return answer_list

    @staticmethod
    def input_to_squad_examples(question: str, contexts: List[Context]) -> List[DataExample]:
        """Convert input passage and question into a DataExample."""
        examples = []
        for idx, ctx in enumerate(contexts):
            examples.append(
                DataExample(
                    qas_id=str(idx),
                    question_text=question,
                    context_text=ctx.text,
                    answer_text=[],
                    start_position_character=None,
                    title="",
                    is_impossible=False,
                    answers=[]
                )
            )
        return examples

    def compute_predictions_logits(self, all_examples, all_features, all_results,
                                   n_best_size, max_answer_length,
                                   do_lower_case, version_2_with_negative,
                                   null_score_diff_threshold, tokenizer, enable_softmax):
        """
        It computs all reader predictions from data
        :param all_examples: pairs of context example and query
        :param all_features: features from examples
        :param all_results: ll results from different document chunks
        :param n_best_size: the size of the final result list
        :param max_answer_length:  maximuim length of the answer text
        :param do_lower_case: whether only convert all words to lower cases
        :param version_2_with_negative:
        :param null_score_diff_threshold:
        :param tokenizer:
        :param enable_softmax: flag of computing softmax
        :return:
        """

        example_index_to_features = collections.defaultdict(list)
        for feature in all_features:
            example_index_to_features[feature.example_index].append(feature)

        unique_id_to_result = {}
        for result in all_results:
            unique_id_to_result[result.unique_id] = result

        _PrelimPrediction = collections.namedtuple("PrelimPrediction",
                                                   ["feature_index", "start_index", "end_index", "start_logit",
                                                    "end_logit"])

        all_predictions = collections.OrderedDict()
        all_nbest_json = collections.OrderedDict()
        scores_diff_json = collections.OrderedDict()

        for (example_index, example) in enumerate(all_examples):
            features = example_index_to_features[example_index]
            if len(features) == 0:
                continue

            prelim_predictions = []
            # keep track of the minimum score of null start+end of position 0
            score_null = 1000000  # large and positive
            min_null_feature_index = 0  # the paragraph slice with min null score
            null_start_logit = 0  # the start logit at the slice with min null score
            null_end_logit = 0  # the end logit at the slice with min null score

            for (feature_index, feature) in enumerate(features):
                result = unique_id_to_result[feature.unique_id]
                start_indexes = self._get_best_indexes(result.start_logits, n_best_size)
                end_indexes = self._get_best_indexes(result.end_logits, n_best_size)
                # if we could have irrelevant answers, get the min score of irrelevant
                if version_2_with_negative:
                    feature_null_score = result.start_logits[0] + result.end_logits[0]
                    if feature_null_score < score_null:
                        score_null = feature_null_score
                        min_null_feature_index = feature_index
                        null_start_logit = result.start_logits[0]
                        null_end_logit = result.end_logits[0]

                for start_index in start_indexes:
                    for end_index in end_indexes:
                        # We could hypothetically create invalid predictions, e.g., predict
                        # that the start of the span is in the question. We throw out all
                        # invalid predictions.
                        if start_index >= len(feature.tokens):
                            continue
                        if end_index >= len(feature.tokens):
                            continue
                        if start_index not in feature.token_to_orig_map:
                            continue
                        if end_index not in feature.token_to_orig_map:
                            continue
                        if not feature.token_is_max_context.get(start_index, False):
                            continue
                        if end_index < start_index:
                            continue
                        length = end_index - start_index + 1
                        if length > max_answer_length:
                            continue
                        prelim_predictions.append(
                            _PrelimPrediction(
                                feature_index=feature_index,
                                start_index=start_index,
                                end_index=end_index,
                                start_logit=result.start_logits[start_index],
                                end_logit=result.end_logits[end_index]))

            if version_2_with_negative:
                prelim_predictions.append(
                    _PrelimPrediction(
                        feature_index=min_null_feature_index,
                        start_index=0,
                        end_index=0,
                        start_logit=null_start_logit,
                        end_logit=null_end_logit,
                    )
                )
            prelim_predictions = sorted(prelim_predictions, key=lambda x: (x.start_logit + x.end_logit), reverse=True)

            _NbestPrediction = collections.namedtuple("NbestPrediction",
                                                      ["text", "start_logit", "end_logit", "start_index", "end_index"])

            seen_predictions = {}
            nbest = []
            for pred in prelim_predictions:
                if len(nbest) >= n_best_size:
                    break
                feature = features[pred.feature_index]
                if pred.start_index > 0:  # this is a non-null prediction
                    tok_tokens = feature.tokens[pred.start_index: (pred.end_index + 1)]
                    orig_doc_start = feature.token_to_orig_map[pred.start_index]
                    orig_doc_end = feature.token_to_orig_map[pred.end_index]
                    orig_tokens = example.doc_tokens[orig_doc_start: (orig_doc_end + 1)]

                    tok_text = tokenizer.convert_tokens_to_string(tok_tokens)

                    # De-tokenize WordPieces that have been split off.
                    tok_text = tok_text.replace(" ##", "")
                    tok_text = tok_text.replace("##", "")

                    # Clean whitespace
                    tok_text = tok_text.strip()
                    tok_text = " ".join(tok_text.split())
                    orig_text = " ".join(orig_tokens)

                    final_text = self.get_final_text(tok_text, orig_text, do_lower_case)
                    if "##" in final_text or "[UNK]" in final_text:
                        print(final_text, "||", tok_text, "||", orig_text)
                    if final_text in seen_predictions:
                        continue
                    seen_predictions[final_text] = True
                else:
                    # continue
                    final_text = ""
                    seen_predictions[final_text] = True

                nbest.append(_NbestPrediction(text=final_text, start_logit=pred.start_logit, end_logit=pred.end_logit,
                                              start_index=pred.start_index, end_index=pred.end_index))

            # if we didn't include the empty option in the n-best, include it
            if version_2_with_negative:
                if "" not in seen_predictions:
                    nbest.append(_NbestPrediction(text="", start_logit=null_start_logit, end_logit=null_end_logit,
                                                  start_index=pred.start_index, end_index=pred.end_index))

                # In very rare edge cases we could only have single null prediction.
                # So we just create a nonce prediction in this case to avoid failure.
                if len(nbest) == 1:
                    nbest.insert(0, _NbestPrediction(text="empty", start_logit=0.0, end_logit=0.0,
                                                     start_index=0, end_index=0))

            # In very rare edge cases we could have no valid predictions. So we
            # just create a nonce prediction in this case to avoid failure.
            if not nbest:
                nbest.append(_NbestPrediction(text="empty", start_logit=0.0, end_logit=0.0,
                                              start_index=0, end_index=0))
            assert len(nbest) >= 1, "No valid predictions"

            total_scores = []
            best_non_null_entry = None
            for entry in nbest:
                total_scores.append(entry.start_logit + entry.end_logit)
                if not best_non_null_entry:
                    if entry.text:
                        best_non_null_entry = entry
            probs = total_scores

            nbest_json = []
            for (i, entry) in enumerate(nbest):
                output = collections.OrderedDict()

                output["text"] = entry.text
                output["probability"] = probs[i]
                output["start_logit"] = entry.start_logit
                output["end_logit"] = entry.end_logit
                output["start_index"] = entry.start_index
                output["end_index"] = entry.end_index
                output["doc_idx"] = example.qas_id
                nbest_json.append(output)

            assert len(nbest_json) >= 1, "No valid predictions"

            if best_non_null_entry:
                if not version_2_with_negative:
                    all_predictions[example.qas_id] = (nbest_json[0]["text"],
                                                       nbest_json[0]['probability'])
                else:
                    # predict "" iff the null score - the score of best non-null > threshold
                    score_diff = score_null - best_non_null_entry.start_logit - (best_non_null_entry.end_logit)
                    scores_diff_json[example.qas_id] = score_diff

                    if score_diff > null_score_diff_threshold:
                        all_predictions[example.qas_id] = {"text": "", "probability": 0.0, "start_logit": 0.0, "end_logit": 0.0,
                                                           "start_index": 0, "end_index": 0, "doc_idx": example.qas_id}
                    else:
                        all_predictions[example.qas_id] = {"text": best_non_null_entry.text,
                                                           "probability": best_non_null_entry.start_logit + best_non_null_entry.end_logit,
                                                           "start_logit": best_non_null_entry.start_logit,
                                                           "end_logit": best_non_null_entry.end_logit,
                                                           "start_index": best_non_null_entry.start_index,
                                                           "end_index": best_non_null_entry.end_index,
                                                           "doc_idx": example.qas_id}

                all_nbest_json[example.qas_id] = nbest_json

        return all_predictions, all_nbest_json

    @staticmethod
    def _get_best_indexes(logits, n_best_size):
        """
        Get the n-best logits from a list.
        :param logits: a list of logits
        :param n_best_size: number of best from the list
        :return: a list of n-best logit indexes
        """

        index_and_score = sorted(enumerate(logits), key=lambda x: x[1], reverse=True)

        best_indexes = []
        for idx, _ in enumerate(index_and_score):
            if idx >= n_best_size:
                break
            best_indexes.append(index_and_score[idx][0])
        return best_indexes

    @staticmethod
    def get_final_text(pred_text, orig_text, do_lower_case):
        """
        Project the tokenized prediction back to the original text.
        :param pred_text: predicted text
        :param orig_text: original text from the document
        :param do_lower_case: whether consider only lower cases
        :return: (string) generate the final answer in text


        When we created the data, we kept track of the alignment between original
        (whitespace tokenized) tokens and our WordPiece tokenized tokens. So
        now `orig_text` contains the span of our original text corresponding to the
        span that we predicted.

        However, `orig_text` may contain extra characters that we don't want in
        our prediction.

        For example, let's say:
          pred_text = steve smith
          orig_text = Steve Smith's

        We don't want to return `orig_text` because it contains the extra "'s".

        We don't want to return `pred_text` because it's already been normalized
        (the SQuAD eval script also does punctuation stripping/lower casing but
        our tokenizer does additional normalization like stripping accent
        characters).

        What we really want to return is "Steve Smith".

        Therefore, we have to apply a semi-complicated alignment heuristic between
        `pred_text` and `orig_text` to get a character-to-character alignment. This
        can fail in certain cases in which case we just return `orig_text`.
        """

        def _strip_spaces(text):
            ns_chars = []
            ns_to_s_map = collections.OrderedDict()
            for (idx, s_char) in enumerate(text):
                if s_char == " ":
                    continue
                ns_to_s_map[len(ns_chars)] = idx
                ns_chars.append(s_char)
            ns_text = "".join(ns_chars)
            return ns_text, ns_to_s_map

        # We first tokenize `orig_text`, strip whitespace from the result
        # and `pred_text`, and check if they are the same length. If they are
        # NOT the same length, the heuristic has failed. If they are the same
        # length, we assume the characters are one-to-one aligned.
        tokenizer = BasicTokenizer(do_lower_case=do_lower_case)

        tok_text = " ".join(tokenizer.tokenize(orig_text))

        start_position = tok_text.find(pred_text)
        if start_position == -1:
            return orig_text
        end_position = start_position + len(pred_text) - 1

        (orig_ns_text, orig_ns_to_s_map) = _strip_spaces(orig_text)
        (tok_ns_text, tok_ns_to_s_map) = _strip_spaces(tok_text)

        if len(orig_ns_text) != len(tok_ns_text):
            return orig_text

        # We then project the characters in `pred_text` back to `orig_text` using
        # the character-to-character alignment.
        tok_s_to_ns_map = {}
        for (i, tok_index) in tok_ns_to_s_map.items():
            tok_s_to_ns_map[tok_index] = i

        orig_start_position = None
        if start_position in tok_s_to_ns_map:
            ns_start_position = tok_s_to_ns_map[start_position]
            if ns_start_position in orig_ns_to_s_map:
                orig_start_position = orig_ns_to_s_map[ns_start_position]

        if orig_start_position is None:
            return orig_text

        orig_end_position = None
        if end_position in tok_s_to_ns_map:
            ns_end_position = tok_s_to_ns_map[end_position]
            if ns_end_position in orig_ns_to_s_map:
                orig_end_position = orig_ns_to_s_map[ns_end_position]

        if orig_end_position is None:
            return orig_text

        output_text = orig_text[orig_start_position:(orig_end_position + 1)]
        return output_text
