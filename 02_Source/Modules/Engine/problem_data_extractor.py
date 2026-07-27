"""
EduFormula AI
Problem Data Extractor
Version 2.0
"""

import re

from Modules.Problem import ProblemContext


class ProblemDataExtractor:

    def extract(self, problem: str):

        # Chuẩn hóa chuỗi
        text = problem.replace(" ", "")

        # Tìm hàm số dạng:
        # y = 2x + 3
        # y=-5x-7
        match = re.search(
            r"y=([+-]?\d*)x([+-]\d+)?",
            text
        )

        if not match:
            return ProblemContext()

        a = match.group(1)
        b = match.group(2)

        # Chuẩn hóa hệ số a
        if a == "" or a == "+":
            a = 1

        elif a == "-":
            a = -1

        else:
            a = int(a)

        # Chuẩn hóa hệ số b
        if b is None:
            b = 0

        else:
            b = int(b)

        context = ProblemContext()

        context.problem_type = "linear_function"
        context.raw_problem = problem

        context.set("a", a)
        context.set("b", b)

        return context