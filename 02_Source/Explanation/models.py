"""
Explanation Domain Models

BUILD-042B
"""

from dataclasses import dataclass, field


@dataclass
class Explanation:
    title: str = ""
    summary: str = ""
    concept: str = ""
    formula_explanation: str = ""
    variable_explanation: str = ""

    steps: list[str] = field(default_factory=list)
    examples: list[str] = field(default_factory=list)
    tips: list[str] = field(default_factory=list)
    common_mistakes: list[str] = field(default_factory=list)
    learning_notes: list[str] = field(default_factory=list)