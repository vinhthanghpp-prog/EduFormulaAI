from Modules.Engine.problem_analyzer import ProblemAnalyzer

from Modules.Lessons.Math.Grade10.linear_function import get_lesson

lesson = get_lesson()

problem = """
Cho hàm số y = 2x + 3.
"""

engine = ProblemAnalyzer()

result = engine.analyze(
    lesson,
    problem
)

from pprint import pprint

pprint(result)