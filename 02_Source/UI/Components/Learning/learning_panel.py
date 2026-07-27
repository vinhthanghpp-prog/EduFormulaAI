import customtkinter as ctk

from UI.Components.Graph import GraphViewer

from UI.Components.Question.question_panel import QuestionPanel

class LearningPanel(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.graph = GraphViewer(self)

        self.graph.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        self.question = QuestionPanel(self)

        self.question.pack(
            fill="x",
            padx=20,
            pady=10
        )

    def load_step(self, learning_step):

        self.graph.show(
            learning_step.visualization
        )