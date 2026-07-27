from pprint import pprint

from Modules.Evaluation import AnswerChecker


checker = AnswerChecker()

result = checker.check(

    student_answer=" 2 ",

    correct_answer="2"

)

pprint(result.to_dict())