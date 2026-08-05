import unittest

from Content.blocks import (
    ContentBlock,
    ConceptBlock,
)


class TestConceptBlock(unittest.TestCase):

    def test_concept_block_can_be_created(self):
        block = ConceptBlock()

        self.assertIsNotNone(block)

    def test_concept_block_inherits_content_block(self):
        block = ConceptBlock()

        self.assertIsInstance(
            block,
            ContentBlock,
        )

    def test_concept_block_default_type(self):
        block = ConceptBlock()

        self.assertEqual(
            block.type,
            "concept",
        )