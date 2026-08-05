"""
Content Blocks
==============

Educational content block domain models.
"""

from dataclasses import dataclass, field


@dataclass
class ContentBlock:
    id: str = ""
    type: str = ""
    title: str = ""
    content: str = ""
    order: int = 0
    difficulty: str = ""


@dataclass
class ConceptBlock(ContentBlock):
    """Concept content block."""

    type: str = field(default="concept")

@dataclass
class FormulaBlock(ContentBlock):
    """Formula content block."""

    pass

@dataclass
class ExampleBlock(ContentBlock):
    """Example content block."""

    type: str = field(default="example")


@dataclass
class TipBlock(ContentBlock):
    """Tip content block."""

    type: str = field(default="tip")


@dataclass
class WarningBlock(ContentBlock):
    """Warning content block."""

    type: str = field(default="warning")


@dataclass
class SummaryBlock(ContentBlock):
    """Summary content block."""

    type: str = field(default="summary")