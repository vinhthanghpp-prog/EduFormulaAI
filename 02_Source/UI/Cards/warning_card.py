"""
EduFormula AI
Warning Card
"""

import customtkinter as ctk

from UI.Cards.base_card import BaseCard
from UI.Theme import Fonts


class WarningCard(BaseCard):

    def __init__(self, parent, warning):

        super().__init__(
            parent,
            "⚠️ Lưu ý"
        )

        self.warning = warning

        self.build()

    def build(self):

        if hasattr(self.warning, "content"):

            title_text = self.warning.title
            content_text = self.warning.content

        else:

            title_text = self.warning.get(
                "title",
                ""
            )

            content_text = self.warning.get(
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