from pprint import pprint

from Modules.Teaching import TeachingScriptFactory

from Modules.Engine.learning_path_planner import LearningPathPlanner
from Modules.Engine.knowledge_mapper import KnowledgeMapper
from Modules.Engine.problem_parser import ProblemParser
from Modules.Engine.problem_data_extractor import ProblemDataExtractor

from Modules.Lessons.Math.Grade10.linear_function import get_lesson


lesson = get_lesson()

problem = """
Cho hàm số y = 2x + 3.

Hãy xác định chiều của đồ thị.
"""

# -------------------------
# Parser
# -------------------------

parser = ProblemParser()

parser_result = parser.parse(problem)

# -------------------------
# Problem Context
# -------------------------

extractor = ProblemDataExtractor()

context = extractor.extract(problem)

# -------------------------
# Knowledge
# -------------------------

mapper = KnowledgeMapper()

knowledge = mapper.map(
    lesson,
    parser_result
)

# -------------------------
# Learning Path
# -------------------------

planner = LearningPathPlanner()

path = planner.create_path(
    knowledge
)

# -------------------------
# Teaching Script
# -------------------------

factory = TeachingScriptFactory()

script = factory.create(
    path[0],
    lesson,
    context
)

pprint(script.to_dict())