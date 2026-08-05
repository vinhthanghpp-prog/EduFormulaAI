import unittest

from Content.factory import ContentBlockFactory
from Content.blocks import ContentBlock
from Content.blocks import (
    ContentBlock,
    ConceptBlock,
    FormulaBlock,
)


class TestContentBlockFactory(unittest.TestCase):

    def test_factory_can_be_imported(self):
        factory = ContentBlockFactory()

        self.assertIsNotNone(factory)

    def test_factory_has_create(self):
        factory = ContentBlockFactory()

        self.assertTrue(
            hasattr(factory, "create")
        )

    def test_create_accepts_block_type(self):
        factory = ContentBlockFactory()

        result = factory.create("concept")

        self.assertIsInstance(
            result,
            ContentBlock,
        )

    def test_create_returns_content_block(self):
        factory = ContentBlockFactory()

        result = factory.create("concept")

        self.assertIsInstance(
            result,
            ContentBlock,
        )

    def test_create_returns_concept_block(self):
        factory = ContentBlockFactory()

        result = factory.create("concept")

        self.assertIsInstance(
            result,
            ConceptBlock,
        )

    def test_create_returns_formula_block(self):
        factory = ContentBlockFactory()

        result = factory.create("formula")

        self.assertIsInstance(
            result,
            FormulaBlock,
        )