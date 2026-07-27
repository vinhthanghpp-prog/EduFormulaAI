"""
EduFormula AI

Subsystem:
Evaluation

Module:
Answer Result

Version:
1.0
"""


class AnswerResult:

    def __init__(self):

        self.correct = False

        self.score = 0

        self.feedback = ""

        self.normalized_answer = ""

    def to_dict(self):

        return {

            "correct": self.correct,

            "score": self.score,

            "feedback": self.feedback,

            "normalized_answer": self.normalized_answer

        }