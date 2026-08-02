"""
VariableRepository
Quản lý dữ liệu bảng variables
"""

from Database.Repository.base_repository import BaseRepository
from Database.models import Variable
from datetime import datetime


class VariableRepository(BaseRepository):

    def __init__(self, connection=None):

        super().__init__(connection)

    def create(self, variable: Variable) -> int:

        now = datetime.now().isoformat()

        cursor = self.cursor

        cursor.execute(
            """
            INSERT INTO variables
            (
                formula_id,
                symbol,
                name,
                description,
                unit,
                variable_type,
                default_value,
                sort_order,
                status,
                created_at,
                updated_at
            )
            VALUES
            (
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            )
            """,
            (
                variable.formula_id,
                variable.symbol,
                variable.name,
                variable.description,
                variable.unit,
                variable.variable_type,
                variable.default_value,
                variable.sort_order,
                variable.status,
                now,
                now,
            ),
        )

        self.commit()

        return cursor.lastrowid

    def get_by_id(self, variable_id: int) -> Variable | None:

        cursor = self.cursor

        cursor.execute(
            """
            SELECT *
            FROM variables
            WHERE id = ?
            """,
            (variable_id,),
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return Variable(**dict(row))

    def exists_symbol(
        self,
        formula_id: int,
        symbol: str,
    ) -> bool:

        cursor = self.cursor

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM variables
            WHERE formula_id = ?
            AND symbol = ?
            """,
            (
                formula_id,
                symbol,
            ),
        )

        return cursor.fetchone()[0] > 0

    def get_by_formula(
        self,
        formula_id: int,
    ) -> list[Variable]:

        cursor = self.cursor

        cursor.execute(
            """
            SELECT *
            FROM variables
            WHERE formula_id = ?
            ORDER BY sort_order, id
            """,
            (formula_id,),
        )

        rows = cursor.fetchall()

        return [
            Variable(**dict(row))
            for row in rows
        ]

    def update(self, variable: Variable) -> bool:

        cursor = self.cursor

        cursor.execute(
            """
            UPDATE variables
            SET
                formula_id = ?,
                symbol = ?,
                name = ?,
                description = ?,
                unit = ?,
                variable_type = ?,
                default_value = ?,
                sort_order = ?,
                status = ?,
                updated_at = ?
            WHERE id = ?
            """,
            (
                variable.formula_id,
                variable.symbol,
                variable.name,
                variable.description,
                variable.unit,
                variable.variable_type,
                variable.default_value,
                variable.sort_order,
                variable.status,
                datetime.now().isoformat(),
                variable.id,
            ),
        )

        self.commit()

        return cursor.rowcount > 0

    def delete(self, variable_id: int) -> bool:

        cursor = self.cursor

        cursor.execute(
            """
            DELETE FROM variables
            WHERE id = ?
            """,
            (variable_id,),
        )

        self.commit()

        return cursor.rowcount > 0