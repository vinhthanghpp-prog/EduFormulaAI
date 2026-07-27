from Modules.Lessons.Math.lesson_catalog import LESSONS


class LessonCatalogRepository:

    def get_lessons(self, grade):

        return LESSONS.get(grade, [])