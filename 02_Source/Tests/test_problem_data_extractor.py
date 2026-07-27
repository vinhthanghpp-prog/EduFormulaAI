from pprint import pprint

from Modules.Engine.problem_data_extractor import ProblemDataExtractor

problem = """
Cho hàm số

y = 2x + 3

Hãy xác định chiều của đồ thị.
"""

extractor = ProblemDataExtractor()

data = extractor.extract(problem)

pprint(data.to_dict())