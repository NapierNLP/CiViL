
class DataExample(object):

    def __init__(self,
                 qas_id: str,
                 question_text: str,
                 context_text: str,
                 answer_text: list,
                 start_position_character,
                 title,
                 answers=[],
                 is_impossible=False):

        self.qas_id = qas_id
        self.question_text = question_text
        self.context_text = context_text
        self.answer_text = answer_text
        self.title = title
        self.is_impossible = is_impossible
        self.answers = answers

        self.start_position, self.end_position = 0, 0

        doc_tokens = []
        char_to_word_offset = []
        prev_is_whitespace = True

        for c in self.context_text:
            if self._is_whitespace(c):
                prev_is_whitespace = True
            else:
                if prev_is_whitespace:
                    doc_tokens.append(c)
                else:
                    doc_tokens[-1] += c
                prev_is_whitespace = False
            char_to_word_offset.append(len(doc_tokens) - 1)

        self.doc_tokens = doc_tokens
        self.char_to_word_offset = char_to_word_offset

        # Start and end positions only has a value during evaluation.
        if start_position_character is not None and not is_impossible:
            self.start_position = char_to_word_offset[start_position_character]
            self.end_position = char_to_word_offset[
                min(start_position_character + len(answer_text) - 1, len(char_to_word_offset) - 1)
            ]

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        _str = ""
        _str += "qas_id: %s" % self.qas_id
        _str += ", question_text: %s" % (
            self.question_text)
        _str += ", doc_tokens: [%s]" % (" ".join(self.doc_tokens))
        if self.start_position:
            _str += ", start_position: %d" % self.start_position
        if self.end_position:
            _str += ", end_position: %d" % self.end_position
        return _str

    @staticmethod
    def _is_whitespace(char):
        if char == " " or char == "\t" or char == "\r" or char == "\n" or ord(char) == 0x202F:
            return True
        return False

