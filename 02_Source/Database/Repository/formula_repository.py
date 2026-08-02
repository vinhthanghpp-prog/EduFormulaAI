"""
FormulaRepository
Quản lý dữ liệu bảng formulas
"""

from datetime import datetime

from Database.Repository.base_repository import BaseRepository
from Database.models import Formula


class FormulaRepository(BaseRepository):

    def __init__(self, connection=None):

        super().__init__(connection)

    def create(self, formula: Formula) -> int:

        now = datetime.now().isoformat()

        cursor = self.cursor

        cursor.execute(
            """
            INSERT INTO formulas
            (
                knowledge_id,
                code,
                name,
                expression,
                description,
                meaning,
                conditions,
                applications,
                notes,
                difficulty_level,
                sort_order,
                status,
                created_at,
                updated_at
            )
            VALUES
            (
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            )
            """,
            (
                formula.knowledge_id,
                formula.code,
                formula.name,
                formula.expression,
                formula.description,
                formula.meaning,
                formula.conditions,
                formula.applications,
                formula.notes,
                formula.difficulty_level,
                formula.sort_order,
                formula.status,
                now,
                now,
            ),
        )

        self.commit()

        return cursor.lastrowid

    def get_by_id(self, formula_id: int) -> Formula | None:

        cursor = self.cursor

        cursor.execute(
            """
            SELECT *
            FROM formulas
            WHERE id = ?
            """,
            (formula_id,),
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return Formula(**dict(row))

    def exists_code(
        self,
        knowledge_id: int,
        code: str,
    ) -> bool:

        cursor = self.cursor

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM formulas
            WHERE knowledge_id = ?
            AND code = ?
            """,
            (
                knowledge_id,
                code,
            ),
        )

        return cursor.fetchone()[0] > 0

    def get_by_knowledge(
        self,
        knowledge_id: int,
    ) -> list[Formula]:

        cursor = self.cursor

        cursor.execute(
            """
            SELECT *
            FROM formulas
            WHERE knowledge_id = ?
            ORDER BY sort_order, id
            """,
            (knowledge_id,),
        )

        rows = cursor.fetchall()

        return [
            Formula(**dict(row))
            for row in rows
        ]

    def update(self, formula: Formula) -> bool:

        cursor = self.cursor

        cursor.execute(
            """
            UPDATE formulas
            SET
                knowledge_id = ?,
                code = ?,
                name = ?,
                expression = ?,
                description = ?,
                meaning = ?,
                conditions = ?,
                applications = ?,
                notes = ?,
                difficulty_level = ?,
                sort_order = ?,
                status = ?,
                updated_at = ?
            WHERE id = ?
            """,
            (
                formula.knowledge_id,
                formula.code,
                formula.name,
                formula.expression,
                formula.description,
                formula.meaning,
                formula.conditions,
                formula.applications,
                formula.notes,
                formula.difficulty_level,
                formula.sort_order,
                formula.status,
                datetime.now().isoformat(),
                formula.id,
            ),
        )

        self.commit()

        return cursor.rowcount > 0

    def delete(self, formula_id: int) -> bool:

        cursor = self.cursor

        cursor.execute(
            """
            DELETE FROM formulas
            WHERE id = ?
            """,
            (formula_id,),
        )

        self.commit()

        return cursor.rowcount > 0