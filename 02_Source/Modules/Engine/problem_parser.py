"""
EduFormula AI
Problem Parser
Version 1.0
"""


class ProblemParser:

    """
    Phân tích yêu cầu của đề bài.
    """

    INTENT_RULES = {

        "đi lên": "graph_direction",
        "đi xuống": "graph_direction",
        "chiều": "graph_direction",
        "đồ thị": "graph_analysis",

        "hệ số góc": "identify_slope",
        "hệ số a": "identify_slope",

        "tung độ gốc": "identify_intercept",
        "hệ số b": "identify_intercept"
    }

    def parse(self, problem: str):

        text = problem.lower()

        keywords = []

        intent = "unknown"

        for key, value in self.INTENT_RULES.items():

            if key in text:

                keywords.append(key)

                if intent == "unknown":
                    intent = value

        return {

            "intent": intent,

            "keywords": keywords
        }