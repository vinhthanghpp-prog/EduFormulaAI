import unittest

from Content.lesson_loader import LessonLoader
from Content.models import LearningContent


class TestLessonLoader(unittest.TestCase):

    def test_loader_can_be_created(self):

        loader = LessonLoader()

        self.assertIsNotNone(loader)

    def test_loader_has_load(self):

        loader = LessonLoader()

        self.assertTrue(
            hasattr(loader, "load")
        )

    def test_load_accepts_path_parameter(self):

        loader = LessonLoader()

        result = loader.load("Data/Lessons/lesson.md")

        self.assertIsNotNone(result)

    def test_load_reads_file(self):

        loader = LessonLoader()

        result = loader.load("Data/Lessons/lesson.md")

        self.assertGreater(
            len(result.learning_units),
            0,
        )

    def test_load_returns_learning_content(self):

        loader = LessonLoader()

        result = loader.load("Data/Lessons/lesson.md")

        self.assertIsInstance(
            result,
            LearningContent,
        )