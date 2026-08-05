import unittest

from Content.blocks import ContentBlock, TipBlock


class TestTipBlock(unittest.TestCase):

    def test_tip_block(self):
        block = TipBlock()

        self.assertIsNotNone(block)
        self.assertIsInstance(block, ContentBlock)
        self.assertEqual(block.type, "tip")