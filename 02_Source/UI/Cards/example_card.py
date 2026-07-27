"""
EduFormula AI
Example Card
"""

import customtkinter as ctk

from UI.Cards.base_card import BaseCard
from UI.Theme import Fonts


class ExampleCard(BaseCard):

    def __init__(self, parent, example):

        super().__init__(
            parent,
            "🧠 Ví dụ"
        )

        self.example = example

        self.build()

    def build(self):

        # ==========================
        # Tiêu đề ví dụ
        # ==========================

        title = ctk.CTkLabel(
            self.body,
            text=self.example.get(
                "title",
                ""
            ),
            font=Fonts.CARD_TITLE
        )

        title.pack(
            anchor="w",
            pady=(5, 10)
        )

        # ==========================
        # Nội dung
        # ==========================

        content = ctk.CTkLabel(
            self.body,
            text=self.example.get(
                "content",
                ""
            ),
            justify="left",
            wraplength=760
        )

        content.pack(
            anchor="w"
        )