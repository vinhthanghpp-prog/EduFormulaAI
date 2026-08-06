from Content.models import (
    LearningContent,
    LearningUnit,
)
from Content.metadata_builder import MetadataBuilder


class LearningContentBuilder:

    def build(self, source, blocks):

        content = LearningContent()

        metadata_builder = MetadataBuilder()

        content.metadata = metadata_builder.build(source)

        unit = LearningUnit()

        unit.content_blocks = blocks

        content.learning_units.append(unit)

        return content