"""
EduFormula AI
Lesson Repository
Version : 1.0
"""

from Modules.Lessons.Math.Grade10.linear_function import get_lesson


class LessonRepository:

    def __init__(self):
        pass

    def get_math_grade10_lesson1(self):
        """
        Trả về bài học Hàm số bậc nhất.
        """
        return get_lesson()

    def get_lesson(self, subject, grade, lesson_id):
        """
        Hàm tổng quát.
        Hiện tại MVP chỉ có một bài.
        Sau này sẽ mở rộng.
        """

        if (
            subject == "Toán"
            and grade == 10
            and lesson_id == 1
        ):
            return self.get_math_grade10_lesson1()

        return None