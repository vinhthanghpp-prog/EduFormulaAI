"""
EduFormula AI
Formula Card
"""

import customtkinter as ctk

from UI.Cards.base_card import BaseCard
from UI.Theme import Fonts


class FormulaCard(BaseCard):

    def __init__(self, parent, formula):

        super().__init__(
            parent,
            "📐 Công thức"
        )

        self.load(formula)

    def load(self, formula):

        expression = formula.get(
            "expression",
            ""
        )

        description = formula.get(
            "description",
            ""
        )

        expression_label = ctk.CTkLabel(
            self.body,
            text=expression,
            font=Fonts.TITLE
        )

        expression_label.pack(
            pady=(10, 20)
        )

        description_label = ctk.CTkLabel(
            self.body,
            text=description,
            justify="left",
            wraplength=700
        )

        description_label.pack(
            anchor="w"
        )