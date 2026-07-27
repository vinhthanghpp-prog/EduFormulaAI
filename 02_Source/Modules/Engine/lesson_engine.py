"""
EduFormula AI
Lesson Engine
Version : 1.0
"""

from Modules.Repository import LessonRepository


class LessonEngine:

    def __init__(self):
        self.repository = LessonRepository()

    def open_lesson(self, subject, grade, lesson_id):
        """
        Mở một bài học.
        """

        lesson = self.repository.get_lesson(
            subject,
            grade,
            lesson_id
        )

        return lesson