"""
EduFormula AI

Cognitive Engine

Version 1.0
"""


from Modules.Cognitive import SkillDiagnoser


class CognitiveEngine:

    def __init__(self):

        self.diagnoser = SkillDiagnoser()

    def analyze(

        self,

        step,

        answer_result

    ):

        return self.diagnoser.diagnose(

            step,

            answer_result

        )