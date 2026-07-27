"""
EduFormula AI
Teaching Script Model
Version 1.0
"""


class TeachingScript:

    def __init__(self):

        self.explanation = ""

        self.visualization = None

        self.question = ""

        self.answer = ""

        self.feedback = ""

        self.hint = ""

        self.transition = ""

    def to_dict(self):

        return {

            "explanation": self.explanation,

            "visualization": self.visualization,

            "question": self.question,

            "answer": self.answer,

            "feedback": self.feedback,

            "hint": self.hint,

            "transition": self.transition

        }