from pprint import pprint

from Modules.Cognitive import CognitiveEngine
from Modules.Evaluation import AnswerChecker

checker = AnswerChecker()

answer = checker.check(

    "3",

    "2"

)

step = {

    "skill": "identify_variable"

}

engine = CognitiveEngine()

result = engine.analyze(

    step,

    answer

)

pprint(result.to_dict())