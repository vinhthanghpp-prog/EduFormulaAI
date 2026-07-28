from __future__ import annotations

from Database.Repository.chapter_repository import ChapterRepository
from Database.models import Chapter
from Database.Repository.grade_repository import GradeRepository


class ChapterService:

    def __init__(
        self,
        repository: ChapterRepository | None = None,
    ) -> None:

        self.repository = repository or ChapterRepository()

    def create_chapter(
        self,
        grade_id: int,
        code: str,
        name: str,
        description: str = "",
        sort_order: int = 0,
    ) -> Chapter:

        code = code.strip()
        name = name.strip()

        if not code:
            raise ValueError("Chapter code cannot be empty.")

        if not name:
            raise ValueError("Chapter name cannot be empty.")

        grade_repo = GradeRepository(self.repository.conn)

        if grade_repo.get_by_id(grade_id) is None:
            raise ValueError("Grade does not exist.")

        if self.repository.exists_code(grade_id, code):
            raise ValueError(f"Chapter code '{code}' already exists.")

        chapter = Chapter(
            id=None,
            grade_id=grade_id,
            code=code,
            name=name,
            description=description,
            sort_order=sort_order,
            status=1,
        )

        chapter_id = self.repository.create(chapter)

        return self.repository.get_by_id(chapter_id)