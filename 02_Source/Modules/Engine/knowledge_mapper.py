"""
EduFormula AI
Knowledge Mapper
Version 1.0
"""


class KnowledgeMapper:
    """
    Ánh xạ Intent -> Kiến thức cần học
    """

    def map(self, lesson: dict, parser_result: dict):

        intent = parser_result.get("intent", "unknown")

        knowledge = {
            "intent": intent,
            "concepts": [],
            "rules": [],
            "skills": []
        }

        # ===== Hàm số bậc nhất =====

        if intent == "graph_direction":

            knowledge["concepts"] = [
                lesson["concept"]["content"]
            ]

            knowledge["rules"] = [
                "Nếu a > 0 thì đồ thị đi lên.",
                "Nếu a < 0 thì đồ thị đi xuống."
            ]

            knowledge["skills"] = [
                "identify_variable",
                "compare_number",
                "draw_conclusion"
            ]

        elif intent == "identify_slope":

            knowledge["concepts"] = [
                "Hệ số a quyết định độ dốc của đường thẳng."
            ]

            knowledge["skills"] = [
                "identify_variable"
            ]

        elif intent == "identify_intercept":

            knowledge["concepts"] = [
                "Hệ số b quyết định tung độ gốc."
            ]

            knowledge["skills"] = [
                "identify_variable"
            ]

        return knowledge