"""
EduFormula AI
Navigation Controller
"""

from Modules.Engine import LessonEngine


class NavigationController:

    def __init__(self, lesson_viewer):

        self.lesson_viewer = lesson_viewer
        self.lesson_engine = LessonEngine()

    def open_lesson(self, subject, grade, lesson_id):

        lesson = self.lesson_engine.open_lesson(
            subject,
            grade,
            lesson_id
        )

        if lesson is not None:
            self.lesson_viewer.load_lesson(lesson)