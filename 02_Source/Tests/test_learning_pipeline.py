from pprint import pprint

from Modules.Pipeline import LearningPipeline

from Modules.Lessons.Math.Grade10.linear_function import get_lesson


lesson = get_lesson()

problem = """
Cho hàm số

y = 2x + 3

Hãy xác định chiều của đồ thị.
"""

pipeline = LearningPipeline()

script = pipeline.process(
    lesson,
    problem
)

print(type(script))
print(script)

if script is not None:
    pprint(script.to_dict())