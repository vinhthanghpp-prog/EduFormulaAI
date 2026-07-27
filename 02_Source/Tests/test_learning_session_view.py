import customtkinter as ctk

from Modules.Engine.learning_engine import LearningEngine
from Modules.Lessons.Math.Grade10.linear_function import get_lesson

from UI.Components.learning_session_view import LearningSessionView


lesson = get_lesson()

problem = """
Cho hàm số y = 2x + 3.

Hãy xác định chiều của đồ thị.
"""

engine = LearningEngine()

session = engine.start(
    lesson,
    problem
)

app = ctk.CTk()

app.geometry("600x500")

view = LearningSessionView(app)

view.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)

view.load_session(session)

app.mainloop()