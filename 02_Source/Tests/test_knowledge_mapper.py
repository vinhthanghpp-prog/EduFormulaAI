from pprint import pprint

from Modules.Engine.problem_parser import ProblemParser
from Modules.Engine.knowledge_mapper import KnowledgeMapper

from Modules.Lessons.Math.Grade10.linear_function import get_lesson

lesson = get_lesson()

problem = """
Cho hàm số y = 2x + 3.

Hãy xác định chiều của đồ thị.
"""

parser = ProblemParser()
parser_result = parser.parse(problem)

mapper = KnowledgeMapper()

result = mapper.map(
    lesson,
    parser_result
)

pprint(result)