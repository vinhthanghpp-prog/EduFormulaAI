"""
EduFormula AI
Variable Card
"""

import customtkinter as ctk

from UI.Cards.base_card import BaseCard
from UI.Theme import Fonts


class VariableCard(BaseCard):

    def __init__(self, parent, variable):

        super().__init__(
            parent,
            f"🧩 {variable.get('symbol', '')}"
        )

        self.variable = variable

        self.build()

    def build(self):

        # ===== Tên =====

        name = ctk.CTkLabel(
            self.body,
            text=self.variable.get(
                "name",
                ""
            ),
            font=Fonts.CARD_TITLE
        )

        name.pack(
            anchor="w",
            pady=(5, 10)
        )

        # ===== Ý nghĩa =====

        meaning_title = ctk.CTkLabel(
            self.body,
            text="Ý nghĩa",
            font=Fonts.BUTTON
        )

        meaning_title.pack(anchor="w")

        meaning = ctk.CTkLabel(
            self.body,
            text=self.variable.get(
                "meaning",
                ""
            ),
            justify="left",
            wraplength=700
        )

        meaning.pack(
            anchor="w",
            pady=(0, 10)
        )

        # ===== Ảnh hưởng =====

        effect_title = ctk.CTkLabel(
            self.body,
            text="Ảnh hưởng",
            font=Fonts.BUTTON
        )

        effect_title.pack(anchor="w")

        effect = ctk.CTkLabel(
            self.body,
            text=self.variable.get(
                "effect",
                ""
            ),
            justify="left",
            wraplength=700
        )

        effect.pack(
            anchor="w",
            pady=(0, 10)
        )

        # ===== Đơn vị =====

        unit_title = ctk.CTkLabel(
            self.body,
            text="Đơn vị",
            font=Fonts.BUTTON
        )

        unit_title.pack(anchor="w")

        unit = self.variable.get(
            "unit",
            ""
        )

        if not unit:
            unit = "Không có"

        unit_label = ctk.CTkLabel(
            self.body,
            text=unit
        )

        unit_label.pack(
            anchor="w",
            pady=(0, 10)
        )

        # ===== Tips =====

        tips = self.variable.get(
            "tips",
            []
        )

        if tips:

            tips_title = ctk.CTkLabel(
                self.body,
                text="💡 Mẹo",
                font=Fonts.BUTTON
            )

            tips_title.pack(anchor="w")

            for tip in tips:

                lbl = ctk.CTkLabel(
                    self.body,
                    text="• " + tip,
                    justify="left",
                    wraplength=700
                )

                lbl.pack(anchor="w")