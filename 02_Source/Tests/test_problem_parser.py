from Modules.Engine.problem_parser import ProblemParser

parser = ProblemParser()

problem = """
Cho hàm số y = 2x + 3.

Hãy xác định chiều của đồ thị.
"""

result = parser.parse(problem)

from pprint import pprint

pprint(result)