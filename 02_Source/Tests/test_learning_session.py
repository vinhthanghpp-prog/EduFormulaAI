from pprint import pprint

from Modules.Engine.problem_parser import ProblemParser
from Modules.Engine.knowledge_mapper import KnowledgeMapper
from Modules.Engine.learning_path_planner import LearningPathPlanner
from Modules.Engine.learning_session import LearningSession

from Modules.Lessons.Math.Grade10.linear_function import get_lesson


lesson = get_lesson()

problem = """
Cho hàm số y = 2x + 3.

Hãy xác định chiều của đồ thị.
"""

# Parser

parser = ProblemParser()

parser_result = parser.parse(problem)

# Mapper

mapper = KnowledgeMapper()

knowledge = mapper.map(
    lesson,
    parser_result
)

# Planner

planner = LearningPathPlanner()

path = planner.create_path(knowledge)

# Session

session = LearningSession(path)

print("=== STEP HIỆN TẠI ===")

pprint(session.current_step())

print()

print("=== HOÀN THÀNH STEP 1 ===")

session.complete_current_step()

pprint(session.current_step())

print()

print("=== THÊM LỖI ===")

session.add_mistake("identify_variable")

pprint(session.get_progress())