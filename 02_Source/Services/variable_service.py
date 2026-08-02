"""
VariableService
Business logic cho Variable
"""

from Database.Repository.variable_repository import VariableRepository
from Database.models import Variable
from Database.Repository.formula_repository import FormulaRepository


class VariableService:

    def __init__(self, connection=None):

        self.repository = VariableRepository(connection)

    def create(self, variable: Variable) -> int:

        if variable.formula_id <= 0:
            raise ValueError("Invalid formula.")

        if not variable.symbol.strip():
            raise ValueError("Symbol is required.")

        if not variable.name.strip():
            raise ValueError("Name is required.")

        formula_repo = FormulaRepository(self.repository.conn)

        if formula_repo.get_by_id(variable.formula_id) is None:
            raise ValueError("Formula does not exist.")

        if self.repository.exists_symbol(
            variable.formula_id,
            variable.symbol,
        ):
            raise ValueError("Symbol already exists.")

        return self.repository.create(variable)