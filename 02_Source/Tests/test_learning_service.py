from pprint import pprint

from Modules.Services import LearningService
from Modules.Lessons.Math.Grade10.linear_function import get_lesson


lesson = get_lesson()

problem = """
Cho hàm số

y = 2x + 3

Hãy xác định chiều của đồ thị.
"""

service = LearningService()

session = service.create_session(
    lesson,
    problem
)

script = service.next_script(
    session
)

pprint(script.to_dict())