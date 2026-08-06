import unittest

from Content.builder import LearningContentBuilder
from Content.models import LearningContent


class TestLearningContentBuilder(unittest.TestCase):

    def test_builder_returns_learning_content(self):

        builder = LearningContentBuilder()

        result = builder.build("", [])

        self.assertIsInstance(
            result,
            LearningContent,
        )

    def test_builder_creates_one_learning_unit(self):

        builder = LearningContentBuilder()

        result = builder.build("", [])

        self.assertEqual(
            len(result.learning_units),
            1,
        )

    def test_builder_assigns_blocks_to_learning_unit(self):

        builder = LearningContentBuilder()

        blocks = [
            "block1",
            "block2",
        ]

        result = builder.build("", blocks)

        self.assertEqual(
            len(result.learning_units[0].content_blocks),
            2,
        )