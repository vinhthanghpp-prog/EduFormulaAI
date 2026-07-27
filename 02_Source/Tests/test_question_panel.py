import customtkinter as ctk

from Modules.Engine.question_factory import QuestionFactory
from Modules.Engine.problem_parser import ProblemParser
from Modules.Engine.knowledge_mapper import KnowledgeMapper
from Modules.Engine.learning_path_planner import LearningPathPlanner

from Modules.Lessons.Math.Grade10.linear_function import get_lesson

from UI.Components.Question import QuestionPanel


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


app = ctk.CTk()

app.geometry("700x450")

panel = QuestionPanel(app)

panel.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)

panel.load_question(
    question,
    lambda is_correct, script: print(is_correct)
)

app.mainloop()