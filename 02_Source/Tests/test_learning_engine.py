from pprint import pprint

from Modules.Engine.learning_engine import LearningEngine
from Modules.Lessons.Math.Grade10.linear_function import get_lesson


lesson = get_lesson()

problem = """
Cho hàm số y = 2x + 3.

Hãy xác định chiều của đồ thị.
"""

engine = LearningEngine()

session = engine.start(
    lesson,
    problem
)

print()

print("===== STEP HIỆN TẠI =====")

print()

pprint(
    session.current_step()
)

print()

print("===== TIẾN ĐỘ =====")

print()

pprint(
    session.get_progress()
)