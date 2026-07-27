"""
EduFormula AI

Skill Diagnoser

Version 1.0
"""


from Modules.Cognitive import DiagnosisResult


class SkillDiagnoser:

    def diagnose(

        self,

        step,

        answer_result

    ):

        result = DiagnosisResult()

        result.correct = answer_result.correct

        result.skill = step["skill"]

        if answer_result.correct:

            result.reason = (
                "Đã hoàn thành kỹ năng."
            )

            result.next_action = (
                "next_step"
            )

        else:

            result.reason = (
                "Chưa hoàn thành kỹ năng."
            )

            result.next_action = (
                "show_hint"
            )

        return result