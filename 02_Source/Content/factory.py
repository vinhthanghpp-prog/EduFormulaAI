"""
Content Block Factory
=====================

Factory responsible for creating ContentBlock objects.
"""
from Content.blocks import (
    ContentBlock,
    ConceptBlock,
    FormulaBlock,
)

BLOCK_TYPES = {
    "concept": ConceptBlock,
    "formula": FormulaBlock,
}


class ContentBlockFactory:
    """Factory for creating content blocks."""

    def create(self, block_type):
        block_class = BLOCK_TYPES.get(block_type, ContentBlock)
        return block_class()