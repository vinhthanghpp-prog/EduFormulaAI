"""
EduFormula AI
Lesson View Renderer
BUILD-048B
"""
from UI.Cards.concept_card import ConceptCard
from Content.blocks import ConceptBlock
from Content.blocks import FormulaBlock
from UI.Cards.formula_card import FormulaCard
from Content.blocks import ExampleBlock
from UI.Cards.example_card import ExampleCard
from Content.blocks import TipBlock
from UI.Cards.tips_card import TipCard
from Content.blocks import WarningBlock
from UI.Cards.warning_card import WarningCard
from Content.blocks import SummaryBlock
from UI.Cards.summary_card import SummaryCard

class LessonViewRenderer:

    def __init__(self, parent):
        self.parent = parent

    def render(self, blocks):
        """
        BUILD-048B
        GREEN STEP 3

        Hiện tại chỉ bảo toàn số lượng phần tử.
        Chưa chuyển sang Card.
        """

        cards = []

        for block in blocks:

            if isinstance(block, ConceptBlock):

                cards.append(
                    ConceptCard(
                        self.parent,
                        block
                    )
                )

            elif isinstance(block, FormulaBlock):

                cards.append(
                    FormulaCard(
                        self.parent,
                        block
                    )
                )

            elif isinstance(block, ExampleBlock):

                cards.append(
                    ExampleCard(
                        self.parent,
                        block
                    )
                )

            elif isinstance(block, TipBlock):

                cards.append(
                    TipCard(
                        self.parent,
                        block
                    )
                )

            elif isinstance(block, WarningBlock):

                cards.append(
                    WarningCard(
                        self.parent,
                        block
                    )
                )

            elif isinstance(block, SummaryBlock):

                cards.append(
                    SummaryCard(
                        self.parent,
                        block
                    )
                )

            else:

                cards.append(block)

        return cards

import unittest

from Modules.Renderer.lesson_view_renderer import LessonViewRenderer


class TestLessonViewRenderer(unittest.TestCase):

    def test_renderer_can_be_created(self):

        renderer = LessonViewRenderer(None)

        self.assertIsNotNone(renderer)

    def test_renderer_has_render(self):

        renderer = LessonViewRenderer(None)

        self.assertTrue(
            hasattr(renderer, "render")
        )