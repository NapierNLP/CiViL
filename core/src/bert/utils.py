import string
from typing import Mapping, Optional, Any


# @dataclass
class Context:
    """
    Following Bertsrini's setting, it represents a Context or Document to find answer from.
    A text is unspecified with respect to it length; in principle, it
    could be a full-length document, a paragraph-sized passage, or
    even a short phrase.
    Parameters
    ----------
    text : str
        The context that contains potential answer.
    metadata : Mapping[str, Any]
        Additional metadata and other annotations.
    score : Optional[float]
        The score of the context. For example, the score might be the BM25 score
        from an initial retrieval stage.
    """

    def __init__(self,
                 json_object: dict = None,
                 idx: str = None,
                 title: str = None,
                 text: str = None):

        self.idx = idx if not json_object else json_object.get('idx')
        self.title = (title if title else "None") if not json_object else json_object.get('title')
        self.text = text if not json_object else json_object.get('text')

    def toJson(self):
        return {"idx": self.idx, "title": self.title, "text": self.text, "length": len(self.text)}


# @dataclass
class Answer:
    def __init__(self,
                 json_object: dict = None,
                 text: str = None,
                 score: Optional[float] = 0.0,
                 query: {} = None,
                 document: str = None,
                 document_id: str = None,
                 start_index: int = 0,
                 end_index: int = 0,
                 metadata: Mapping[str, Any] = None):

        self.text = self.normalize_answer(text) if not json_object else json_object.get('answer')
        self.score = float(score) if not json_object else json_object.get('score')
        self.query = query if not json_object else json_object.get('query')
        self.document = document if not json_object else json_object.get('document')
        self.document_id = document_id if not json_object else json_object.get('document_id')
        self.start_index = start_index if not json_object else json_object.get('start_index')
        self.end_index = end_index if not json_object else json_object.get('end_index')
        self.metadata = metadata if not json_object else json_object.get('metadata')

    @staticmethod
    def normalize_answer(s):
        """Lower text and remove punctuation, articles and extra whitespace."""

        def white_space_fix(text):
            return " ".join(text.split())

        def remove_punc(text):
            exclude = set(string.punctuation)
            return "".join(ch for ch in text if ch not in exclude)

        def lower(text):
            return text.lower()

        return white_space_fix(remove_punc(lower(s)))

    def toJson(self):
        return {"question:": self.query, "selected_doc": self.document_id, "span": self.text,
                "score": self.score, "length": len(self.text),
                "start_index": self.start_index, "end_index": self.end_index,
                "document_id": self.document_id, "metadata": self.metadata}


# @dataclass
class SquadResult:
    """
    Following Bertsrini's setting, it represents a SquadResult which can be used to evaluate a model's output on the SQuAD dataset.

    Args:
        unique_id: The unique identifier corresponding to that example.
        start_logits: The logits corresponding to the start of the answer
        end_logits: The logits corresponding to the end of the answer
    """

    def __init__(self, unique_id, start_logits, end_logits, start_top_index=None, end_top_index=None, cls_logits=None):
        self.start_logits = start_logits
        self.end_logits = end_logits
        self.unique_id = unique_id

        if start_top_index:
            self.start_top_index = start_top_index
            self.end_top_index = end_top_index
            self.cls_logits = cls_logits
