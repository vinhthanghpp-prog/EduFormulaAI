"""
GradeRepository
BUILD-024A Release
"""

from __future__ import annotations

from typing import Optional

from Database.Repository.base_repository import BaseRepository
from Database.models import Grade


class GradeRepository(BaseRepository):
    """Repository for Grade."""

    TABLE = "grades"

    @staticmethod
    def _to_model(row) -> Grade | None:
        if row is None:
            return None
        return Grade(
            id=row["id"],
            code=row["code"],
            name=row["name"],
            subject_id=row["subject_id"],
            status=row["status"],
            created_at=row["created_at"],
            updated_at=row["updated_at"],
        )

    def create(self, grade: Grade) -> int:
        sql = """
        INSERT INTO grades
        (subject_id, code, name, status, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        cur = self.execute(sql, (
            grade.subject_id,
            grade.code,
            grade.name,
            grade.status,
            grade.created_at,
            grade.updated_at,
        ))
        return int(cur.lastrowid)

    def update(self, grade: Grade) -> None:
        sql = """
        UPDATE grades
        SET subject_id=?,
            code=?,
            name=?,
            status=?,
            updated_at=?
        WHERE id=?
        """
        self.execute(sql, (
            grade.subject_id,
            grade.code,
            grade.name,
            grade.status,
            grade.updated_at,
            grade.id,
        ))

    def delete(self, grade_id: int) -> None:
        self.execute(
            "UPDATE grades SET status=0 WHERE id=?",
            (grade_id,),
        )

    def restore(self, grade_id: int) -> None:
        self.execute(
            "UPDATE grades SET status=1 WHERE id=?",
            (grade_id,),
        )

    def get_by_id(self, grade_id: int) -> Optional[Grade]:
        row = self.fetch_one(
            "SELECT * FROM grades WHERE id=?",
            (grade_id,),
        )
        return self._to_model(row)

    def get_by_subject(self, subject_id: int) -> list[Grade]:
        rows = self.fetch_all(
            "SELECT * FROM grades WHERE subject_id=? ORDER BY code",
            (subject_id,),
        )
        return [self._to_model(r) for r in rows]

    def get_active_by_subject(self, subject_id: int) -> list[Grade]:
        rows = self.fetch_all(
            """
            SELECT * FROM grades
            WHERE subject_id=? AND status=1
            ORDER BY code
            """,
            (subject_id,),
        )
        return [self._to_model(r) for r in rows]

    def exists_code(self, subject_id: int, code: str) -> bool:
        row = self.fetch_one(
            """
            SELECT 1
            FROM grades
            WHERE subject_id=? AND code=?
            LIMIT 1
            """,
            (subject_id, code),
        )
        return row is not None

    def get_by_code(self, subject_id: int, code: str) -> Optional[Grade]:
        row = self.fetch_one(
            """
            SELECT *
            FROM grades
            WHERE subject_id=? AND code=?
            """,
            (subject_id, code),
        )
        return self._to_model(row)

    def search(self, subject_id: int, keyword: str) -> list[Grade]:
        rows = self.fetch_all(
            """
            SELECT *
            FROM grades
            WHERE subject_id=?
              AND (code LIKE ? OR name LIKE ?)
            ORDER BY code
            """,
            (subject_id, f"%{keyword}%", f"%{keyword}%"),
        )
        return [self._to_model(r) for r in rows]
