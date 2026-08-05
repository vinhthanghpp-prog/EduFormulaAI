import unittest

from Content.blocks import ContentBlock, WarningBlock


class TestWarningBlock(unittest.TestCase):

    def test_warning_block(self):
        block = WarningBlock()

        self.assertIsNotNone(block)
        self.assertIsInstance(block, ContentBlock)
        self.assertEqual(block.type, "warning")