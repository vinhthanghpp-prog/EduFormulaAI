"""
FormulaService
Business logic cho Formula
"""

from Database.Repository.formula_repository import FormulaRepository
from Database.Repository.knowledge_repository import KnowledgeRepository
from Database.models import Formula


class FormulaService:

    def __init__(self, connection=None):

        self.repository = FormulaRepository(connection)

        self.knowledge_repository = KnowledgeRepository(connection)

    def create(self, formula: Formula) -> int:

        if formula.knowledge_id <= 0:
            raise ValueError("Knowledge không hợp lệ.")

        if self.knowledge_repository.get_by_id(formula.knowledge_id) is None:
            raise ValueError("Knowledge không tồn tại.")

        if not formula.code.strip():
            raise ValueError("Code không được để trống.")

        if not formula.name.strip():
            raise ValueError("Tên Formula không được để trống.")

        if not formula.expression.strip():
            raise ValueError("Biểu thức Formula không được để trống.")

        if self.repository.exists_code(
            formula.knowledge_id,
            formula.code,
        ):
            raise ValueError("Code đã tồn tại.")

        return self.repository.create(formula)