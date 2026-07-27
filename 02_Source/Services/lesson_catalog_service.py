from Modules.Repository import LessonCatalogRepository


class LessonCatalogService:

    def __init__(self):
        self.repository = LessonCatalogRepository()

    def get_lessons(self, grade):
        return self.repository.get_lessons(grade)