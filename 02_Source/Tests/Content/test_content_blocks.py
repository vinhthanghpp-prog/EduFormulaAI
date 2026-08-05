import unittest

from Content.blocks import ContentBlock


class TestContentBlock(unittest.TestCase):

    def test_content_block_can_be_created(self):
        block = ContentBlock()

        self.assertIsNotNone(block)

    def test_content_block_has_id(self):
        block = ContentBlock()

        self.assertEqual(
            block.id,
            "",
        )

    def test_content_block_has_type(self):
        block = ContentBlock()

        self.assertEqual(
            block.type,
            "",
        )

    def test_content_block_has_title(self):
        block = ContentBlock()

        self.assertEqual(
            block.title,
            "",
        )

    def test_content_block_has_content(self):
        block = ContentBlock()

        self.assertEqual(
            block.content,
            "",
        )

    def test_content_block_has_order(self):
        block = ContentBlock()

        self.assertEqual(
            block.order,
            0,
        )

    def test_content_block_has_difficulty(self):
        block = ContentBlock()

        self.assertEqual(
            block.difficulty,
            "",
        )