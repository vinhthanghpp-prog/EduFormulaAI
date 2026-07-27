"""
EduFormula AI
Lesson Viewer
Version: LV-002
"""

import customtkinter as ctk

from UI.Cards import (
    ObjectiveCard,
    FormulaCard,
    VariableCard,
)


class LessonViewer(ctk.CTkScrollableFrame):

    def __init__(self, parent):

        super().__init__(parent)

    def clear(self):

        for widget in self.winfo_children():
            widget.destroy()

    def load_lesson(self, lesson):

        self.clear()

        # =====================================================
        # Tiêu đề
        # =====================================================

        title = ctk.CTkLabel(
            self,
            text=lesson["metadata"]["title"],
            font=("Segoe UI", 28, "bold")
        )

        title.pack(
            pady=(20, 20)
        )

        # =====================================================
        # Objective Card
        # =====================================================

        objective_card = ObjectiveCard(
            self,
            lesson["objectives"]
        )

        objective_card.pack(
            fill="x",
            padx=20,
            pady=10
        )

        # =====================================================
        # Formula Card
        # =====================================================

        formula_card = FormulaCard(
            self,
            lesson["formula"]
        )

        formula_card.pack(
            fill="x",
            padx=20,
            pady=10
        )

        # =====================================================
        # Variable Cards
        # =====================================================

        for variable in lesson.get("variables", []):

            card = VariableCard(
                self,
                variable
            )

            card.pack(
                fill="x",
                padx=20,
                pady=10
            )

        # =====================================================
        # Khái niệm
        # =====================================================

        concept_title = ctk.CTkLabel(
            self,
            text="📖 Khái niệm",
            font=("Segoe UI", 18, "bold")
        )

        concept_title.pack(
            anchor="w",
            padx=20,
            pady=(20, 5)
        )

        concept = ctk.CTkLabel(
            self,
            text=lesson["concept"]["content"],
            wraplength=850,
            justify="left"
        )

        concept.pack(
            anchor="w",
            padx=20
        )

        # =====================================================
        # Ví dụ
        # =====================================================

        example_title = ctk.CTkLabel(
            self,
            text="🧠 Ví dụ",
            font=("Segoe UI", 18, "bold")
        )

        example_title.pack(
            anchor="w",
            padx=20,
            pady=(20, 5)
        )

        example = ctk.CTkLabel(
            self,
            text=lesson["example"]["content"],
            wraplength=850,
            justify="left"
        )

        example.pack(
            anchor="w",
            padx=20,
            pady=(0, 20)
        )