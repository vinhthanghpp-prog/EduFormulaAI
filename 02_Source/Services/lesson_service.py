from __future__ import annotations

from Database.Repository.lesson_repository import LessonRepository
from Database.Repository.chapter_repository import ChapterRepository
from Database.models import Lesson


class LessonService:

    def __init__(
        self,
        repository: LessonRepository | None = None,
    ) -> None:

        self.repository = repository or LessonRepository()

    def create_lesson(
        self,
        chapter_id: int,
        code: str,
        name: str,
        description: str = "",
        learning_time: int = 45,
        sort_order: int = 0,
    ) -> Lesson:

        code = code.strip()
        name = name.strip()

        if not code:
            raise ValueError("Lesson code cannot be empty.")

        if not name:
            raise ValueError("Lesson name cannot be empty.")

        chapter_repo = ChapterRepository(self.repository.conn)

        if chapter_repo.get_by_id(chapter_id) is None:
            raise ValueError("Chapter does not exist.")

        if self.repository.exists_code(chapter_id, code):
            raise ValueError(f"Lesson code '{code}' already exists.")

        lesson = Lesson(
            id=None,
            chapter_id=chapter_id,
            code=code,
            name=name,
            description=description,
            learning_time=learning_time,
            sort_order=sort_order,
            status=1,
        )

        lesson_id = self.repository.create(lesson)

        return self.repository.get_by_id(lesson_id)