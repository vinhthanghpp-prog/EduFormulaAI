"""
EduFormula AI

Answer Normalizer

Version 1.0
"""


class AnswerNormalizer:

    def normalize(
        self,
        answer
    ):

        if answer is None:
            return ""

        text = str(answer)

        text = text.lower()

        text = text.strip()

        return text