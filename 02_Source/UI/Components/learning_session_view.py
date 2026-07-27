"""
EduFormula AI
Learning Session View
Version 1.0
"""

import customtkinter as ctk

from Modules.Engine.question_factory import QuestionFactory
from UI.Components.Question import QuestionPanel


class LearningSessionView(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        self.session = None

        self.question_factory = QuestionFactory()

    # -------------------------------------------------

    def load_session(self, session):

        self.session = session

        self.refresh()

    # -------------------------------------------------

    def refresh(self):

        for widget in self.winfo_children():
            widget.destroy()

        if self.session is None:
            return

        step = self.session.current_step()

        if step is None:

            finish = ctk.CTkLabel(

                self,

                text="🎉 Bạn đã hoàn thành bài học.",

                font=("Segoe UI",18,"bold")

            )

            finish.pack(
                pady=20
            )

            return

        # =========================================

        title = ctk.CTkLabel(

            self,

            text="🎓 Phiên học",

            font=("Segoe UI",20,"bold")

        )

        title.pack(
            pady=(15,5)
        )

        # =========================================

        step_title = ctk.CTkLabel(

            self,

            text=step["title"],

            font=("Segoe UI",18,"bold")

        )

        step_title.pack()

        # =========================================

        goal = ctk.CTkLabel(

            self,

            text="Mục tiêu:\n" + step["goal"],

            justify="left"

        )

        goal.pack(
            pady=10
        )

        # ========================================

        question = self.question_factory.create(
            step,
            self.session
        )

        panel = QuestionPanel(self)

        panel.pack(
            fill="x",
            padx=20,
            pady=10
        )

        panel.load_question(
            question,
            self.on_answer_checked
        )

        # =========================================

        progress = self.session.get_progress()

        progress_label = ctk.CTkLabel(

            self,

            text=f"Bước {progress['completed']+1}/{progress['total']}"

        )

        progress_label.pack()

    def on_answer_checked(
            self,
            is_correct,
            script
    ):

        if is_correct:

            self.show_success()

    def show_success(self):

        for widget in self.winfo_children():
            widget.destroy()

        label = ctk.CTkLabel(
            self,
            text="🎉 Chính xác!\n\nEm đã hoàn thành bước này.",
            font=("Segoe UI", 16, "bold")
        )
        label.pack(pady=20)

        button = ctk.CTkButton(
            self,
            text="Tiếp tục",
            command=self.continue_learning
        )
        button.pack(pady=10)


    def continue_learning(self):

        self.session.complete_current_step()

        self.refresh()