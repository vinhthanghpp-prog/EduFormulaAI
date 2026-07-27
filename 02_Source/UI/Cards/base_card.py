import customtkinter as ctk

from UI.Theme import Fonts, Radius, Spacing


class BaseCard(ctk.CTkFrame):

    def __init__(self, parent, title):

        super().__init__(
            parent,
            corner_radius=Radius.CARD
        )

        self.title = ctk.CTkLabel(
            self,
            text=title,
            font=Fonts.CARD_TITLE
        )

        self.title.pack(
            anchor="w",
            padx=Spacing.LARGE,
            pady=(Spacing.LARGE, Spacing.MEDIUM)
        )

        self.body = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.body.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, Spacing.LARGE)
        )