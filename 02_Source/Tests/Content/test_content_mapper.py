import unittest

from Content.mapper import ContentMapper
from Content.models import LearningContent


class FakeLesson:
    def __init__(self):
        self.name = "Vector Addition"

class TestContentMapper(unittest.TestCase):

    def test_mapper_can_be_created(self):
        mapper = ContentMapper()

        self.assertIsNotNone(mapper)

    def test_mapper_has_map_lesson(self):
        mapper = ContentMapper()

        self.assertTrue(hasattr(mapper, "map_lesson"))

    def test_map_lesson_accepts_lesson_parameter(self):
        mapper = ContentMapper()

        self.assertEqual(
            mapper.map_lesson.__code__.co_argcount,
            2,
        )

    def test_map_lesson_returns_learning_content(self):
        mapper = ContentMapper()

        result = mapper.map_lesson(None)

        self.assertIsInstance(result, LearningContent)

    def test_map_lesson_maps_metadata_lesson(self):
        mapper = ContentMapper()

        lesson = FakeLesson()

        content = mapper.map_lesson(lesson)

        self.assertEqual(
            content.metadata.lesson,
            "Vector Addition",
        )

    def test_map_lesson_returns_initialized_metadata(self):
        mapper = ContentMapper()

        content = mapper.map_lesson(None)

        self.assertIsNotNone(content.metadata)


if __name__ == "__main__":
    unittest.main()