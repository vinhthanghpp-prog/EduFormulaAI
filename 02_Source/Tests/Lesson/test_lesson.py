import unittest

from Content.models import LearningContent


class TestLesson(unittest.TestCase):

    def test_lesson_can_be_created(self):

        lesson = LearningContent()

        self.assertIsNotNone(lesson)