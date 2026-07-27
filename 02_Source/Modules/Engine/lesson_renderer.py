"""
EduFormula AI
Dynamic Lesson Renderer
"""

from UI.Cards import CARD_REGISTRY
from UI.Theme import Spacing


class LessonRenderer:

    def __init__(self, viewer):

        self.viewer = viewer

    def clear(self):

        for widget in self.viewer.winfo_children():
            widget.destroy()

    def render(self, lesson):

        self.clear()

        for section_name, card_class in CARD_REGISTRY.items():

            data = lesson.get(section_name)

            if not data:
                continue

            card = card_class(
                self.viewer,
                data
            )

            card.pack(
                fill="x",
                padx=Spacing.LARGE,
                pady=Spacing.MEDIUM
            )