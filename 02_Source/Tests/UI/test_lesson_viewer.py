import unittest

from UI.lesson_viewer import LessonViewer
from Content.models import LearningContent


class TestLessonViewer(unittest.TestCase):

    def test_viewer_can_be_created(self):

        viewer = LessonViewer()

        self.assertIsNotNone(viewer)

    def test_viewer_has_load_lesson(self):

        viewer = LessonViewer()

        self.assertTrue(
            hasattr(viewer, "load_lesson")
        )

    def test_viewer_accepts_learning_content(self):

        viewer = LessonViewer()

        content = LearningContent()

        viewer.load_lesson(content)

        self.assertIs(
            viewer.lesson,
            content,
        )

    def test_viewer_keeps_metadata(self):

        from Content.models import LearningContent

        content = LearningContent()

        content.metadata.subject = "Toán"
        content.metadata.grade = "10"
        content.metadata.chapter = "Vector"
        content.metadata.lesson = "Khái niệm Vector"

        viewer = LessonViewer()

        viewer.load_lesson(content)

        self.assertEqual(
            viewer.lesson.metadata.subject,
            "Toán",
        )

        self.assertEqual(
            viewer.lesson.metadata.grade,
            "10",
        )

        self.assertEqual(
            viewer.lesson.metadata.chapter,
            "Vector",
        )

        self.assertEqual(
            viewer.lesson.metadata.lesson,
            "Khái niệm Vector",
        )

    def test_viewer_returns_lesson_title(self):

        from Content.models import LearningContent

        content = LearningContent()
        content.metadata.lesson = "Khái niệm Vector"

        viewer = LessonViewer()
        viewer.load_lesson(content)

        self.assertEqual(
            viewer.get_lesson_title(),
            "Khái niệm Vector",
        )

    def test_viewer_returns_content_blocks(self):

        from Content.models import (
            LearningContent,
            LearningUnit,
        )

        from Content.blocks import ConceptBlock

        content = LearningContent()

        unit = LearningUnit()

        block = ConceptBlock()
        block.content = "Vector là đại lượng có hướng."

        unit.content_blocks.append(block)

        content.learning_units.append(unit)

        viewer = LessonViewer()

        viewer.load_lesson(content)

        self.assertEqual(
            len(viewer.get_content_blocks()),
            1,
        )