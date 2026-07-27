"""
EduFormula AI
Lesson Renderer
Version 1.0
"""

from UI.Cards import CARD_REGISTRY


class LessonRenderer:

    def __init__(self, parent):

        self.parent = parent

    def render(self, lesson):

        self.render_objectives(lesson)

        self.render_formula(lesson)

        self.render_variables(lesson)

    # -------------------------

    def render_objectives(self, lesson):

        objectives = lesson.get("objectives", [])

        if not objectives:
            return

        card = CARD_REGISTRY["objectives"](
            self.parent,
            objectives
        )

        card.pack(
            fill="x",
            padx=20,
            pady=10
        )

    # -------------------------

    def render_formula(self, lesson):

        formula = lesson.get("formula")

        if not formula:
            return

        card = CARD_REGISTRY["formula"](
            self.parent,
            formula
        )

        card.pack(
            fill="x",
            padx=20,
            pady=10
        )

    # -------------------------

    def render_variables(self, lesson):

        variables = lesson.get(
            "variables",
            []
        )

        for variable in variables:

            card = CARD_REGISTRY["variables"](
                self.parent,
                variable
            )

            card.pack(
                fill="x",
                padx=20,
                pady=10
            )