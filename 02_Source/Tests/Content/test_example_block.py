import unittest

from Content.blocks import ContentBlock, ExampleBlock


class TestExampleBlock(unittest.TestCase):

    def test_example_block(self):
        block = ExampleBlock()

        self.assertIsNotNone(block)
        self.assertIsInstance(block, ContentBlock)
        self.assertEqual(block.type, "example")