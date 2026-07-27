from datetime import datetime

from Database.Repository.base_repository import BaseRepository
from Database.models import Lesson


class LessonRepository(BaseRepository):

    def __init__(self):
        super().__init__()

    def exists_code(self, chapter_id: int, code: str) -> bool:
        cursor = self.cursor

        cursor.execute(
            """
            SELECT 1
            FROM lessons
            WHERE chapter_id = ?
            AND code = ?
            LIMIT 1
            """,
            (chapter_id, code),
        )

        return cursor.fetchone() is not None

    def add_lesson(self, lesson: Lesson) -> int:
        now = datetime.now().isoformat()

        cursor = self.cursor

        cursor.execute(
            """
            INSERT INTO lessons
            (
                chapter_id,
                code,
                name,
                description,
                learning_time,
                sort_order,
                status,
                created_at,
                updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                lesson.chapter_id,
                lesson.code,
                lesson.name,
                lesson.description,
                lesson.learning_time,
                lesson.sort_order,
                lesson.status,
                now,
                now,
            ),
        )

        self.commit()

        return cursor.lastrowid

    def get_by_id(self, lesson_id: int) -> Lesson | None:
        cursor = self.cursor

        cursor.execute(
            """
            SELECT *
            FROM lessons
            WHERE id = ?
            """,
            (lesson_id,),
        )

        row = cursor.fetchone()

        return Lesson(*row) if row else None

    def get_all(self, chapter_id: int | None = None) -> list[Lesson]:
        cursor = self.cursor

        if chapter_id is None:
            cursor.execute("""
                SELECT *
                FROM lessons
                ORDER BY sort_order, code
            """)
        else:
            cursor.execute("""
                SELECT *
                FROM lessons
                WHERE chapter_id = ?
                ORDER BY sort_order, code
            """, (chapter_id,))

        rows = cursor.fetchall()

        return [Lesson(*row) for row in rows]

    def get_by_code(self, chapter_id: int, code: str) -> Lesson | None:
        cursor = self.cursor

        cursor.execute("""
            SELECT *
            FROM lessons
            WHERE chapter_id = ?
            AND code = ?
        """, (chapter_id, code))

        row = cursor.fetchone()

        return Lesson(*row) if row else None

    def update(self, lesson: Lesson) -> bool:
        now = datetime.now().isoformat()

        cursor = self.cursor

        cursor.execute("""
            UPDATE lessons
            SET
                chapter_id = ?,
                code = ?,
                name = ?,
                description = ?,
                learning_time = ?,
                sort_order = ?,
                status = ?,
                updated_at = ?
            WHERE id = ?
        """, (
            lesson.chapter_id,
            lesson.code,
            lesson.name,
            lesson.description,
            lesson.learning_time,
            lesson.sort_order,
            lesson.status,
            now,
            lesson.id,
        ))

        self.commit()

        return cursor.rowcount > 0

    def delete(self, lesson_id: int) -> bool:
        cursor = self.cursor

        cursor.execute("""
            DELETE
            FROM lessons
            WHERE id = ?
        """, (lesson_id,))

        self.commit()

        return cursor.rowcount > 0

    def search(
        self,
        keyword: str,
        chapter_id: int | None = None,
    ) -> list[Lesson]:

        cursor = self.cursor

        keyword = f"%{keyword}%"

        if chapter_id is None:

            cursor.execute("""
                SELECT *
                FROM lessons
                WHERE code LIKE ?
                OR name LIKE ?
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
                FROM lessons
                WHERE chapter_id = ?
                AND (
                        code LIKE ?
                    OR name LIKE ?
                    OR description LIKE ?
                )
                ORDER BY sort_order, code
            """, (
                chapter_id,
                keyword,
                keyword,
                keyword,
            ))

        rows = cursor.fetchall()

        return [Lesson(*row) for row in rows]