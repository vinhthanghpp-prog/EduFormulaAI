from pprint import pprint

from Modules.Engine.question_factory import QuestionFactory
from Modules.Engine.learning_path_planner import LearningPathPlanner
from Modules.Engine.knowledge_mapper import KnowledgeMapper
from Modules.Engine.problem_parser import ProblemParser
from Modules.Lessons.Math.Grade10.linear_function import get_lesson

lesson = get_lesson()

problem = """
Cho hàm số y = 2x + 3.
Hãy xác định chiều của đồ thị.
"""

parser = ProblemParser()
parser_result = parser.parse(problem)

mapper = KnowledgeMapper()
knowledge = mapper.map(lesson, parser_result)

planner = LearningPathPlanner()
path = planner.create_path(knowledge)

factory = QuestionFactory()

question = factory.create(path[0], lesson)

pprint(question.to_dict())