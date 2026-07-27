"""
GradeService
BUILD-024B Release
"""

from __future__ import annotations

from Database.models import Grade
from Database.Repository.grade_repository import GradeRepository
from Services.base_service import BaseService


class GradeService(BaseService):
    """Business logic for Grade."""

    def __init__(self):
        self.repository = GradeRepository()

    # ---------------------------------------------------------
    # Query
    # ---------------------------------------------------------

    def get_all_grades(self, subject_id: int):
        self.require_positive(subject_id, "Subject ID")
        return self.repository.get_by_subject(subject_id)

    def get_active_grades(self, subject_id: int):
        self.require_positive(subject_id, "Subject ID")
        return self.repository.get_active_by_subject(subject_id)

    def get_grade(self, grade_id: int):
        self.require_positive(grade_id, "Grade ID")

        grade = self.repository.get_by_id(grade_id)

        return self.require_entity(
            grade,
            "Không tìm thấy khối lớp."
        )

    def get_grade_by_code(self, subject_id: int, code: str):
        self.require_positive(subject_id, "Subject ID")

        code = self.normalize_code(code)

        return self.repository.get_by_code(subject_id, code)

    def search(self, subject_id: int, keyword: str):
        self.require_positive(subject_id, "Subject ID")

        keyword = self.require_text(keyword, "Từ khóa")

        return self.repository.search(subject_id, keyword)

    # ---------------------------------------------------------
    # Validation
    # ---------------------------------------------------------

    def validate(self, grade: Grade):

        self.require_entity(
            grade,
            "Grade không được để trống."
        )

        self.require_positive(
            grade.subject_id,
            "Subject ID"
        )

        grade.code = self.normalize_code(grade.code)

        grade.name = self.require_text(
            grade.name,
            "Tên khối"
        )

        return grade

    # ---------------------------------------------------------
    # Create
    # ---------------------------------------------------------

    def create_grade(self, grade: Grade):

        grade = self.validate(grade)

        self.validate_duplicate(
            self.repository.exists_code(
                grade.subject_id,
                grade.code
            ),
            f"Mã khối '{grade.code}' đã tồn tại."
        )

        new_id = self.repository.create(grade)

        return self.repository.get_by_id(new_id)

    # ---------------------------------------------------------
    # Update
    # ---------------------------------------------------------

    def update_grade(self, grade: Grade):

        grade = self.validate(grade)

        old = self.repository.get_by_id(grade.id)

        self.require_entity(
            old,
            "Không tìm thấy khối lớp."
        )

        duplicate = self.repository.get_by_code(
            grade.subject_id,
            grade.code
        )

        if duplicate and duplicate.id != grade.id:
            raise ValueError(
                f"Mã khối '{grade.code}' đã tồn tại."
            )

        self.repository.update(grade)

        return self.repository.get_by_id(grade.id)

    # ---------------------------------------------------------
    # Delete
    # ---------------------------------------------------------

    def delete_grade(self, grade_id: int):

        self.require_positive(
            grade_id,
            "Grade ID"
        )

        grade = self.repository.get_by_id(grade_id)

        self.require_entity(
            grade,
            "Không tìm thấy khối lớp."
        )

        self.repository.delete(grade_id)

        return True