import unittest

from Modules.Engine.lesson_renderer import LessonRenderer
from Content.models import (
    LearningContent,
    LearningUnit,
)
from Content.blocks import ConceptBlock


class TestLessonRenderer(unittest.TestCase):

    def test_renderer_can_be_created(self):

        renderer = LessonRenderer()

        self.assertIsNotNone(renderer)

    def test_renderer_has_render(self):

        renderer = LessonRenderer()

        self.assertTrue(
            hasattr(renderer, "render")
        )

    def test_render_returns_list(self):

        renderer = LessonRenderer()

        content = LearningContent()

        unit = LearningUnit()

        unit.content_blocks.append(
            ConceptBlock(content="Vector")
        )

        content.learning_units.append(unit)

        cards = renderer.render(content)

        self.assertIsInstance(cards, list)

    def test_render_preserves_block_count(self):

        renderer = LessonRenderer()

        content = LearningContent()

        unit = LearningUnit()

        unit.content_blocks.append(
            ConceptBlock(content="A")
        )

        unit.content_blocks.append(
            ConceptBlock(content="B")
        )

        content.learning_units.append(unit)

        cards = renderer.render(content)

        self.assertEqual(
            len(cards),
            2
        )