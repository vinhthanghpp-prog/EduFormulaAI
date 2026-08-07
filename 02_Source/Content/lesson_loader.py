from Content.parser import ContentParser
from Content.builder import LearningContentBuilder


class LessonLoader:

    def load(self, path):

        with open(path, "r", encoding="utf-8") as file:
            source = file.read()

        parser = ContentParser()
        blocks = parser.parse(source)

        builder = LearningContentBuilder()

        return builder.build(source, blocks)