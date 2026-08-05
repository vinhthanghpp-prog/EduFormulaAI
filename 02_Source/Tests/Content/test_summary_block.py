import unittest

from Content.blocks import ContentBlock, SummaryBlock


class TestSummaryBlock(unittest.TestCase):

    def test_summary_block(self):
        block = SummaryBlock()

        self.assertIsNotNone(block)
        self.assertIsInstance(block, ContentBlock)
        self.assertEqual(block.type, "summary")