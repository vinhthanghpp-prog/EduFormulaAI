from datetime import datetime

from Database.Repository.base_repository import BaseRepository
from Database.models import Chapter


class ChapterRepository(BaseRepository):

    def __init__(self):
        super().__init__()

    def exists_code(self, grade_id: int, code: str) -> bool:
        cursor = self.cursor

        cursor.execute(
            """
            SELECT 1
            FROM chapters
            WHERE grade_id = ?
            AND code = ?
            LIMIT 1
            """,
            (grade_id, code),
        )

        return cursor.fetchone() is not None

    def add_chapter(self, chapter: Chapter) -> int:
        now = datetime.now().isoformat()

        cursor = self.cursor

        cursor.execute(
            """
            INSERT INTO chapters
            (
                grade_id,
                code,
                name,
                description,
                sort_order,
                status,
                created_at,
                updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                chapter.grade_id,
                chapter.code,
                chapter.name,
                chapter.description,
                chapter.sort_order,
                chapter.status,
                now,
                now,
            ),
        )

        self.commit()

        return cursor.lastrowid

    def get_by_id(self, chapter_id: int) -> Chapter | None:
        cursor = self.cursor

        cursor.execute(
            """
            SELECT *
            FROM chapters
            WHERE id = ?
            """,
            (chapter_id,),
        )

        row = cursor.fetchone()

        return Chapter(*row) if row else None

    def get_all(self, grade_id: int | None = None) -> list[Chapter]:
        cursor = self.cursor

        if grade_id is None:
            cursor.execute("""
                SELECT *
                FROM chapters
                ORDER BY sort_order, code
            """)
        else:
            cursor.execute("""
                SELECT *
                FROM chapters
                WHERE grade_id = ?
                ORDER BY sort_order, code
            """, (grade_id,))

        rows = cursor.fetchall()

        return [Chapter(*row) for row in rows]

    def get_by_code(self, grade_id: int, code: str) -> Chapter | None:
        cursor = self.cursor

        cursor.execute("""
            SELECT *
            FROM chapters
            WHERE grade_id = ?
            AND code = ?
        """, (grade_id, code))

        row = cursor.fetchone()

        return Chapter(*row) if row else None

    def update(self, chapter: Chapter) -> bool:
        now = datetime.now().isoformat()

        cursor = self.cursor

        cursor.execute("""
            UPDATE chapters
            SET
                grade_id = ?,
                code = ?,
                name = ?,
                description = ?,
                sort_order = ?,
                status = ?,
                updated_at = ?
            WHERE id = ?
        """, (
            chapter.grade_id,
            chapter.code,
            chapter.name,
            chapter.description,
            chapter.sort_order,
            chapter.status,
            now,
            chapter.id,
        ))

        self.commit()

        return cursor.rowcount > 0

    def delete(self, chapter_id: int) -> bool:
        cursor = self.cursor

        cursor.execute("""
            DELETE
            FROM chapters
            WHERE id = ?
        """, (chapter_id,))

        self.commit()

        return cursor.rowcount > 0

    def search(
        self,
        keyword: str,
        grade_id: int | None = None,
    ) -> list[Chapter]:

        cursor = self.cursor

        keyword = f"%{keyword}%"

        if grade_id is None:

            cursor.execute("""
                SELECT *
                FROM chapters
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
                FROM chapters
                WHERE grade_id = ?
                AND (
                        code LIKE ?
                    OR name LIKE ?
                    OR description LIKE ?
                )
                ORDER BY sort_order, code
            """, (
                grade_id,
                keyword,
                keyword,
                keyword,
            ))

        rows = cursor.fetchall()

        return [Chapter(*row) for row in rows]