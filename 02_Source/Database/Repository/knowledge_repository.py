from datetime import datetime

from Database.Repository.base_repository import BaseRepository
from Database.models import Knowledge


class KnowledgeRepository(BaseRepository):

    def __init__(self):
        super().__init__()

    def exists_code(self, lesson_id: int, code: str) -> bool:
        cursor = self.cursor

        cursor.execute(
            """
            SELECT 1
            FROM knowledge
            WHERE lesson_id = ?
            AND code = ?
            LIMIT 1
            """,
            (lesson_id, code),
        )

        return cursor.fetchone() is not None

    def add_knowledge(self, knowledge: Knowledge) -> int:
        now = datetime.now().isoformat()

        cursor = self.cursor

        cursor.execute(
            """
            INSERT INTO knowledge
            (
                lesson_id,
                code,
                title,
                description,
                knowledge_type,
                difficulty_level,
                sort_order,
                status,
                created_at,
                updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                knowledge.lesson_id,
                knowledge.code,
                knowledge.title,
                knowledge.description,
                knowledge.knowledge_type,
                knowledge.difficulty_level,
                knowledge.sort_order,
                knowledge.status,
                now,
                now,
            ),
        )

        self.commit()

        return cursor.lastrowid

    def get_by_id(self, knowledge_id: int) -> Knowledge | None:
        cursor = self.cursor

        cursor.execute(
            """
            SELECT *
            FROM knowledge
            WHERE id = ?
            """,
            (knowledge_id,),
        )

        row = cursor.fetchone()

        return Knowledge(*row) if row else None

    def get_all(self, lesson_id: int | None = None) -> list[Knowledge]:
        cursor = self.cursor

        if lesson_id is None:
            cursor.execute("""
                SELECT *
                FROM knowledge
                ORDER BY sort_order, code
            """)
        else:
            cursor.execute("""
                SELECT *
                FROM knowledge
                WHERE lesson_id = ?
                ORDER BY sort_order, code
            """, (lesson_id,))

        rows = cursor.fetchall()

        return [Knowledge(*row) for row in rows]

    def get_by_code(self, lesson_id: int, code: str) -> Knowledge | None:
        cursor = self.cursor

        cursor.execute("""
            SELECT *
            FROM knowledge
            WHERE lesson_id = ?
            AND code = ?
        """, (
            lesson_id,
            code,
        ))

        row = cursor.fetchone()

        return Knowledge(*row) if row else None

    def update(self, knowledge: Knowledge) -> bool:
        now = datetime.now().isoformat()

        cursor = self.cursor

        cursor.execute("""
            UPDATE knowledge
            SET
                lesson_id = ?,
                code = ?,
                title = ?,
                description = ?,
                knowledge_type = ?,
                difficulty_level = ?,
                sort_order = ?,
                status = ?,
                updated_at = ?
            WHERE id = ?
        """, (
            knowledge.lesson_id,
            knowledge.code,
            knowledge.title,
            knowledge.description,
            knowledge.knowledge_type,
            knowledge.difficulty_level,
            knowledge.sort_order,
            knowledge.status,
            now,
            knowledge.id,
        ))

        self.commit()

        return cursor.rowcount > 0

    def delete(self, knowledge_id: int) -> bool:
        cursor = self.cursor

        cursor.execute("""
            DELETE
            FROM knowledge
            WHERE id = ?
        """, (knowledge_id,))

        self.commit()

        return cursor.rowcount > 0

    def search(
        self,
        keyword: str,
        lesson_id: int | None = None,
    ) -> list[Knowledge]:

        cursor = self.cursor

        keyword = f"%{keyword}%"

        if lesson_id is None:

            cursor.execute("""
                SELECT *
                FROM knowledge
                WHERE code LIKE ?
                OR title LIKE ?
                OR description LIKE ?
                ORDER BY sort_order, code
            """, (
                keyword,
                keyword,
                keyword,
            ))

        else:

            cursor.execute("""
                SELECT *
                FROM knowledge
                WHERE lesson_id = ?
                AND (
                        code LIKE ?
                    OR title LIKE ?
                    OR description LIKE ?
                )
                ORDER BY sort_order, code
            """, (
                lesson_id,
                keyword,
                keyword,
                keyword,
            ))

        rows = cursor.fetchall()

        return [Knowledge(*row) for row in rows]