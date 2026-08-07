"""
EduFormula AI
Summary Card
"""

import customtkinter as ctk

from UI.Cards.base_card import BaseCard
from UI.Theme import Fonts


class SummaryCard(BaseCard):

    def __init__(self, parent, summary):

        super().__init__(
            parent,
            "📝 Tóm tắt"
        )

        self.summary = summary

        self.build()

    def build(self):

        if hasattr(self.summary, "content"):

            title_text = self.summary.title
            content_text = self.summary.content

        else:

            title_text = self.summary.get(
                "title",
                ""
            )

            content_text = self.summary.get(
                "content",
                ""
            )

        title = ctk.CTkLabel(
            self.body,
            text=title_text,
            font=Fonts.CARD_TITLE
        )

        title.pack(
            anchor="w",
            pady=(5, 10)
        )

        content = ctk.CTkLabel(
            self.body,
            text=content_text,
            justify="left",
            wraplength=760
        )

        content.pack(
            anchor="w"
        )