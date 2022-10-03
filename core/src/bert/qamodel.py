import logging

import torch

try:
    from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
except ImportError:
    raise ImportError("""
    Bart will be released through pip in v 3.0.0, until then use it by installing from source:

    git clone git@github.com:huggingface/transformers.git
    git checkout d6de6423
    cd transformers
    pip install -e ".[dev]"
    """)


class BertQA:

    def __init__(self, component_config: dict, logger: logging, **kwargs):
        self.component_config = component_config.get('BertReader')
        self._logger = logger

        self.device = torch.device("cuda" if torch.cuda.is_available() and self.component_config.get('on_gpu')
                                   else "cpu") if not kwargs else kwargs.get('device')

        # load the BERT pre-trained model and tokenizer for QA
        _model = AutoModelForQuestionAnswering.from_pretrained(self.component_config.get('model')).to(self.device)
        _tokenizer = AutoTokenizer.from_pretrained(self.component_config.get('model'))
        self._pipeline = pipeline('question-answering', model=_model, tokenizer=_tokenizer)

    def predict(self, question: str, context: list):

        score = 0.0
        res = {}
        for cotxt in context:
            _qa_input = {'question': question, 'context': cotxt}
            new_res = self._pipeline(_qa_input)
            print(new_res)

            if new_res.get('score') > score:
                score = new_res.get('score')
                res = new_res

        return {'text': res.get('answer') if res.get('answer') else 'sorry, i don\'t understand it', 'score': res.get('score')}


if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
    )
    logger = logging.getLogger(__name__)

    qa = BertQA(component_config={"BertReader":{"model": "deepset/tinyroberta-squad2", "on_gpu": "True"}}, logger=logger)
    result = qa.predict(question='Why is model conversion important?', context='The option to convert models between FARM and transformers gives freedom to the user and let people easily switch between frameworks.')
    print(result)