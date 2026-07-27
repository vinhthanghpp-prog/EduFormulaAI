"""
Unit Test
GradeService
BUILD-024B Enterprise Edition
"""

from unittest import TestCase
from unittest.mock import MagicMock

from Database.models import Grade
from Services.grade_service import GradeService


class TestGradeService(TestCase):

    def setUp(self):
        self.service = GradeService()

        # Mock Repository
        self.repository = MagicMock()

        self.service.repository = self.repository

    # =====================================================
    # VALIDATION
    # =====================================================

    def test_validate_success(self):

        grade = Grade(
            subject_id=1,
            code="10",
            name="Lớp 10"
        )

        result = self.service.validate(grade)

        self.assertEqual(result.code, "10")
        self.assertEqual(result.name, "Lớp 10")

    def test_validate_empty_code(self):

        grade = Grade(
            subject_id=1,
            code="",
            name="Lớp 10"
        )

        with self.assertRaises(ValueError):
            self.service.validate(grade)

    def test_validate_empty_name(self):

        grade = Grade(
            subject_id=1,
            code="10",
            name=""
        )

        with self.assertRaises(ValueError):
            self.service.validate(grade)

    def test_validate_invalid_subject(self):

        grade = Grade(
            subject_id=0,
            code="10",
            name="Lớp 10"
        )

        with self.assertRaises(ValueError):
            self.service.validate(grade)

    # =====================================================
    # CREATE
    # =====================================================

    def test_create_success(self):

        grade = Grade(
            subject_id=1,
            code="10",
            name="Lớp 10"
        )

        self.repository.exists_code.return_value = False
        self.repository.create.return_value = 99

        created = Grade(
            id=99,
            subject_id=1,
            code="10",
            name="Lớp 10"
        )

        self.repository.get_by_id.return_value = created

        result = self.service.create_grade(grade)

        self.repository.exists_code.assert_called_once_with(1, "10")
        self.repository.create.assert_called_once()
        self.repository.get_by_id.assert_called_once_with(99)

        self.assertEqual(result.id, 99)

    def test_create_duplicate(self):

        grade = Grade(
            subject_id=1,
            code="10",
            name="Lớp 10"
        )

        self.repository.exists_code.return_value = True

        with self.assertRaises(ValueError):
            self.service.create_grade(grade)

        self.repository.create.assert_not_called()

    # =====================================================
    # UPDATE
    # =====================================================

    def test_update_success(self):

        grade = Grade(
            id=5,
            subject_id=1,
            code="10",
            name="Lớp 10"
        )

        self.repository.get_by_id.side_effect = [
            grade,
            grade
        ]

        self.repository.get_by_code.return_value = None

        result = self.service.update_grade(grade)

        self.repository.update.assert_called_once_with(grade)

        self.assertEqual(result.id, 5)

    def test_update_duplicate(self):

        current = Grade(
            id=5,
            subject_id=1,
            code="10",
            name="Lớp 10"
        )

        duplicate = Grade(
            id=8,
            subject_id=1,
            code="10",
            name="Lớp 10A"
        )

        self.repository.get_by_id.return_value = current
        self.repository.get_by_code.return_value = duplicate

        with self.assertRaises(ValueError):
            self.service.update_grade(current)

    # =====================================================
    # DELETE
    # =====================================================

    def test_delete_success(self):

        grade = Grade(
            id=5,
            subject_id=1,
            code="10",
            name="Lớp 10"
        )

        self.repository.get_by_id.return_value = grade

        result = self.service.delete_grade(5)

        self.repository.delete.assert_called_once_with(5)

        self.assertTrue(result)

    def test_delete_not_found(self):

        self.repository.get_by_id.return_value = None

        with self.assertRaises(ValueError):
            self.service.delete_grade(5)

    # =====================================================
    # QUERY
    # =====================================================

    def test_get_grade(self):

        grade = Grade(
            id=1,
            subject_id=1,
            code="10",
            name="Lớp 10"
        )

        self.repository.get_by_id.return_value = grade

        result = self.service.get_grade(1)

        self.assertEqual(result.id, 1)

    def test_get_grade_by_code(self):

        grade = Grade(
            id=1,
            subject_id=1,
            code="10",
            name="Lớp 10"
        )

        self.repository.get_by_code.return_value = grade

        result = self.service.get_grade_by_code(1, "10")

        self.assertEqual(result.code, "10")

    def test_search(self):

        self.repository.search.return_value = []

        result = self.service.search(1, "10")

        self.assertEqual(result, [])


if __name__ == "__main__":
    import unittest
    unittest.main(verbosity=2)