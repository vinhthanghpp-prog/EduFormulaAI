import unittest

from Content.models import (
    LearningContent,
    Metadata,
    LearningUnit,
)

from Content.models import (
    LearningContent,
    LearningUnit,
    Metadata,
    ContentBlock,
)

class TestLearningContent(unittest.TestCase):

    def test_learning_content_can_be_created(self):
        content = LearningContent()

        self.assertIsNotNone(content)

    def test_metadata_can_be_created(self):
        metadata = Metadata()

        self.assertIsNotNone(metadata)

    def test_learning_unit_can_be_created(self):
        unit = LearningUnit()

        self.assertIsNotNone(unit)

    def test_metadata_default_values(self):
        metadata = Metadata()

        self.assertEqual(metadata.subject, "")
        self.assertEqual(metadata.grade, "")
        self.assertEqual(metadata.chapter, "")
        self.assertEqual(metadata.lesson, "")

    def test_learning_content_default_values(self):
        content = LearningContent()

        self.assertIsInstance(content.metadata, Metadata)

    def test_learning_content_has_empty_learning_units(self):
        content = LearningContent()

        self.assertEqual(len(content.learning_units), 0)

    def test_learning_unit_default_values(self):
        unit = LearningUnit()

        self.assertEqual(unit.title, "")
        self.assertEqual(unit.explanation, "")

    def test_learning_unit_has_empty_content_blocks(self):
        unit = LearningUnit()

        self.assertEqual(len(unit.content_blocks), 0)

    def test_content_block_can_be_created(self):
        block = ContentBlock()

        self.assertIsNotNone(block)


if __name__ == "__main__":
    unittest.main()