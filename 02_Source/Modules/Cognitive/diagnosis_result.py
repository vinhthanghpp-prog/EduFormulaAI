"""
EduFormula AI

Subsystem:
Cognitive

Module:
Diagnosis Result

Version:
1.0
"""


class DiagnosisResult:

    def __init__(self):

        self.correct = False

        self.skill = None

        self.reason = ""

        self.next_action = ""

        self.hint_level = 1

    def to_dict(self):

        return {

            "correct": self.correct,

            "skill": self.skill,

            "reason": self.reason,

            "next_action": self.next_action,

            "hint_level": self.hint_level

        }