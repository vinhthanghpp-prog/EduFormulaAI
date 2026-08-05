"""
Content Mapper

BUILD-041C
Content Engine Foundation
"""

from typing import Any
from Content.models import LearningContent


class ContentMapper:

    
    def map_lesson(self, lesson: Any) -> LearningContent:
        content = LearningContent()

        if lesson is not None:
            content.metadata.lesson = lesson.name

        return content