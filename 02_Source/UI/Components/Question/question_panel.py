"""
EduFormula AI
Question Panel
Version 1.0
"""

import customtkinter as ctk


class QuestionPanel(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        self.callback = None

        self.entry = None

        self.feedback = None

    # ----------------------------

    def load_question(self, script, callback):

        self.callback = callback

        for widget in self.winfo_children():
            widget.destroy()

        # ============================

        title = ctk.CTkLabel(

            self,

            text="❓ Câu hỏi",

            font=("Segoe UI",18,"bold")

        )

        title.pack(
            pady=(10,5)
        )

        # ============================

        q = ctk.CTkLabel(

            self,

            text=script.question,

            wraplength=500,

            justify="left"

        )

        q.pack(
            padx=15,
            pady=10
        )

        # ============================

        self.entry = ctk.CTkEntry(

            self,

            width=250

        )

        self.entry.pack(
            pady=5
        )

        # ============================

        button = ctk.CTkButton(

            self,

            text="Kiểm tra",

            command=lambda: self.check(script)

        )

        button.pack(
            pady=10
        )

        # ============================

        self.feedback = ctk.CTkLabel(

            self,

            text=""

        )

        self.feedback.pack(
            pady=10
        )

    # ----------------------------

    def check(self, script):

        answer = self.entry.get().strip().lower()

        correct = script.answer.strip().lower()

        if answer == correct:

            self.feedback.configure(
            text=script.feedback
        )

            if self.callback:
                self.callback(
                    is_correct=True,
                    script=script
                )

        else:

            self.feedback.configure(

                text="❌ " + script.hint

            )

            if self.callback:
                self.callback(
                    is_correct=False,
                    script=script
                )