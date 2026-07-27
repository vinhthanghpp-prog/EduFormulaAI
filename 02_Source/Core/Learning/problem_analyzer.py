"""
EduFormula AI
Problem Analyzer
Version 1.0
"""


class ProblemAnalyzer:

    """
    Phân tích bài toán để xác định:
    - Chủ đề
    - Công thức
    - Biến
    - Kỹ năng cần sử dụng
    """

    def analyze(self, lesson, problem: str):

        result = {
            "topic": "",
            "formula": "",
            "variables": [],
            "skills": []
        }

        # -------------------------------------------------
        # Phiên bản đầu:
        # Nếu bài học là Hàm số bậc nhất
        # thì trả về dữ liệu tương ứng.
        # -------------------------------------------------

        title = lesson["metadata"]["title"]

        if title == "Hàm số bậc nhất":

            result["topic"] = "Linear Function"

            result["formula"] = "y = ax + b"

            result["variables"] = ["a", "b"]

            result["skills"] = [

                "identify_variable",

                "compare_number",

                "determine_graph_direction"

            ]

        return result