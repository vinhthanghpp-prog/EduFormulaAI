import unittest

from UI.Cards.concept_card import ConceptCard
from UI.Cards.base_card import BaseCard
from Content.blocks import ConceptBlock


class TestConceptCard(unittest.TestCase):

    def test_card_can_be_imported(self):
        self.assertIsNotNone(ConceptCard)

    def test_concept_card_inherits_base_card(self):

        self.assertTrue(
            issubclass(
                ConceptCard,
                BaseCard
            )
        )

    def test_concept_card_stores_concept(self):

        concept = ConceptBlock(
            title="Vector",
            content="Khái niệm Vector"
        )

        card = ConceptCard(
            None,
            concept
        )

        self.assertIs(
            card.concept,
            concept
        )