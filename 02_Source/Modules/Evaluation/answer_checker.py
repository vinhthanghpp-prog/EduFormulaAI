"""
EduFormula AI

Answer Checker

Version 1.0
"""

from Modules.Evaluation import (
    AnswerResult,
    AnswerNormalizer
)


class AnswerChecker:

    def __init__(self):

        self.normalizer = AnswerNormalizer()

    def check(
        self,
        student_answer,
        correct_answer
    ):

        result = AnswerResult()

        student = self.normalizer.normalize(
            student_answer
        )

        correct = self.normalizer.normalize(
            correct_answer
        )

        result.normalized_answer = student

        if student == correct:

            result.correct = True

            result.score = 100

            result.feedback = (
                "🎉 Chính xác!"
            )

        else:

            result.correct = False

            result.score = 0

            result.feedback = (
                "Chưa đúng, hãy thử lại."
            )

        return result