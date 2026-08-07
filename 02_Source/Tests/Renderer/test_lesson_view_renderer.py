import unittest

from Modules.Renderer.lesson_view_renderer import LessonViewRenderer
from Content.blocks import ConceptBlock
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


class TestLessonViewRenderer(unittest.TestCase):

    def test_renderer_can_be_created(self):
        renderer = LessonViewRenderer(None)
        self.assertIsNotNone(renderer)

    def test_renderer_has_render(self):
        renderer = LessonViewRenderer(None)
        self.assertTrue(hasattr(renderer, "render"))

    def test_render_returns_list(self):

        renderer = LessonViewRenderer(None)

        cards = renderer.render([])

        self.assertIsInstance(cards, list)

    def test_render_preserves_block_count(self):

        renderer = LessonViewRenderer(None)

        blocks = [
            ConceptBlock(content="A"),
            ConceptBlock(content="B"),
        ]

        cards = renderer.render(blocks)

        self.assertEqual(
            len(cards),
            2
        )

    def test_render_returns_same_block_type(self):

        renderer = LessonViewRenderer(None)

        block = ConceptBlock(
            title="Vector",
            content="Khái niệm Vector"
        )

        cards = renderer.render([block])

        self.assertIsInstance(
            cards[0],
            ConceptCard
        )

    def test_render_concept_block_returns_concept_card(self):

        renderer = LessonViewRenderer(None)

        block = ConceptBlock(
            title="Vector",
            content="Khái niệm Vector"
        )

        cards = renderer.render([block])

        self.assertIsInstance(
            cards[0],
            ConceptCard
        )

    def test_render_formula_block_returns_formula_card(self):

        renderer = LessonViewRenderer(None)

        block = FormulaBlock(
            title="Định luật II Newton",
            content="F = m × a"
        )

        cards = renderer.render([block])

        self.assertIsInstance(
            cards[0],
            FormulaCard
        )

    def test_render_example_block_returns_example_card(self):

        renderer = LessonViewRenderer(None)

        block = ExampleBlock(
            title="Ví dụ",
            content="Cho m = 2 kg, a = 5 m/s²."
        )

        cards = renderer.render([block])

        self.assertIsInstance(
            cards[0],
            ExampleCard
        )

    def test_render_tip_block_returns_tip_card(self):

        renderer = LessonViewRenderer(None)

        block = TipBlock(
            title="Mẹo",
            content="Đổi đơn vị trước khi thay số."
        )

        cards = renderer.render([block])

        self.assertIsInstance(
            cards[0],
            TipCard
        )

    def test_render_warning_block_returns_warning_card(self):

        renderer = LessonViewRenderer(None)

        block = WarningBlock(
            title="Lưu ý",
            content="Không được bỏ qua đơn vị của đại lượng."
        )

        cards = renderer.render([block])

        self.assertIsInstance(
            cards[0],
            WarningCard
        )

    def test_render_summary_block_returns_summary_card(self):

        renderer = LessonViewRenderer(None)

        block = SummaryBlock(
            title="Tóm tắt",
            content="Lực bằng khối lượng nhân gia tốc."
        )

        cards = renderer.render([block])

        self.assertIsInstance(
            cards[0],
            SummaryCard
        )