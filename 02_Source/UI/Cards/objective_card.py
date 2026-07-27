"""
EduFormula AI
Objective Card
"""

import customtkinter as ctk

from UI.Cards.base_card import BaseCard


class ObjectiveCard(BaseCard):

    def __init__(self, parent, objectives):

        super().__init__(
            parent,
            "🎯 Mục tiêu"
        )

        self.load(objectives)

    def load(self, objectives):

        for objective in objectives:

            label = ctk.CTkLabel(
                self.body,
                text="• " + objective,
                anchor="w",
                justify="left"
            )

            label.pack(
                anchor="w",
                pady=3
            )