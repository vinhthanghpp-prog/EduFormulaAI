"""
EduFormula AI
Learning Path Planner
Version 1.0
"""


class LearningPathPlanner:

    """
    Sinh lộ trình học từ Knowledge Object.
    """

    def create_path(self, knowledge: dict):

        intent = knowledge.get("intent", "unknown")

        path = []

        if intent == "graph_direction":

            path = [

                {
                    "step": 1,
                    "title": "Xác định hệ số a",
                    "goal": "Tìm hệ số góc",
                    "skill": "identify_variable"
                },

                {
                    "step": 2,
                    "title": "So sánh hệ số a với 0",
                    "goal": "Xác định dấu của hệ số",
                    "skill": "compare_number"
                },

                {
                    "step": 3,
                    "title": "Kết luận",
                    "goal": "Xác định chiều đồ thị",
                    "skill": "draw_conclusion"
                }

            ]

        return path