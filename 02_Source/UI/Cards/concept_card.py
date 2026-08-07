"""
EduFormula AI
Concept Card
BUILD-048B
"""

from UI.Cards.base_card import BaseCard


class ConceptCard(BaseCard):

    def __init__(self, parent, concept):

        super().__init__(
            parent,
            "Concept"
        )

        self.concept = concept