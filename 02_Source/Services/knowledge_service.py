from __future__ import annotations

from Database.models import Knowledge
from Database.Repository.knowledge_repository import KnowledgeRepository
from Database.Repository.lesson_repository import LessonRepository


class KnowledgeService:

    def __init__(
        self,
        repository: KnowledgeRepository | None = None,
    ) -> None:

        self.repository = repository or KnowledgeRepository()

    def create_knowledge(
        self,
        lesson_id: int,
        code: str,
        title: str,
        knowledge_type: str,
        description: str = "",
        difficulty_level: int = 1,
        sort_order: int = 0,
        status: int = 1,
    ) -> Knowledge:

        code = code.strip()
        title = title.strip()

        if not code:
            raise ValueError("Knowledge code cannot be empty.")

        if not title:
            raise ValueError("Knowledge title cannot be empty.")

        lesson_repo = LessonRepository(self.repository.conn)

        if lesson_repo.get_by_id(lesson_id) is None:
            raise ValueError("Lesson does not exist.")

        if self.repository.exists_code(
            lesson_id,
            code,
        ):
            raise ValueError(
                f"Knowledge code '{code}' already exists."
            )

        knowledge = Knowledge(
            lesson_id=lesson_id,
            code=code,
            title=title,
            description=description,
            knowledge_type=knowledge_type,
            difficulty_level=difficulty_level,
            sort_order=sort_order,
            status=status,
        )

        knowledge.id = self.repository.create(
            knowledge
        )

        return self.repository.get_by_id(
            knowledge.id
        )