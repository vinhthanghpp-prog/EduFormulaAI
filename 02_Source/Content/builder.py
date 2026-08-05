from Content.models import (
    LearningContent,
    LearningUnit,
)


class LearningContentBuilder:

    def build(self, blocks):

        content = LearningContent()

        unit = LearningUnit()

        unit.content_blocks = blocks

        content.learning_units.append(unit)

        return content