"""
EduFormula AI
Problem Analyzer
Version 2.0
"""


class ProblemAnalyzer:

    def analyze(self, lesson, problem: str):

        metadata = lesson.get("metadata", {})
        formula = lesson.get("formula", {})
        variables = lesson.get("variables", [])
        tips = lesson.get("tips", [])
        mistakes = lesson.get("common_mistakes", [])

        return {

            "lesson_title":
                metadata.get("title", ""),

            "formula":
                formula.get("expression", ""),

            "variables":
                [
                    item["symbol"]
                    for item in variables
                ],

            "tips":
                tips,

            "common_mistakes":
                mistakes
        }