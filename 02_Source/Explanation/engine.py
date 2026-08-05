"""
Explanation Engine

BUILD-042
Explanation Engine Foundation
"""
from Explanation.models import Explanation


class ExplanationEngine:
    """Generate explanations from LearningContent."""

    def generate(self, content):
        explanation = Explanation()

        if content is not None:
            explanation.title = content.metadata.lesson

        return explanation