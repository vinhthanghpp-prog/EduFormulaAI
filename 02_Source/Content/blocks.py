"""
Content Blocks
==============

Educational content block domain models.
"""

from dataclasses import dataclass


@dataclass
class ContentBlock:
    """Base content block."""

    id: str = ""
    type: str = ""
    title: str = ""
    content: str = ""
    order: int = 0
    difficulty: str = ""