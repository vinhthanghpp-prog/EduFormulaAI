from pprint import pprint

from Modules.Learning import LearningStepFactory
from Modules.Lessons.Math.Grade10.linear_function import get_lesson
from Modules.Problem import ProblemContext

lesson = get_lesson()

context = ProblemContext()
context.set("a", 2)
context.set("b", 3)

step = {
    "skill": "identify_variable"
}

factory = LearningStepFactory()

learning_step = factory.create(
    step,
    lesson,
    context
)

print("=== SCRIPT ===")
pprint(learning_step.script.to_dict())

print("\n=== VISUALIZATION ===")
pprint(learning_step.visualization.to_dict())