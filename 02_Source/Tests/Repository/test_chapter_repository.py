"""
test_chapter_repository.py

Unit tests for ChapterRepository.

EduFormula AI
BUILD-025
"""

from __future__ import annotations

from Database.Repository.chapter_repository import ChapterRepository
from Database.models import Chapter

from Tests.test_base import RepositoryTestCase


class TestChapterRepository(RepositoryTestCase):

    # ==========================================================
    # SETUP
    # ==========================================================

    def setUp(self):

        super().setUp()

        self.repo = ChapterRepository(self.conn)

        self.subject_id = self.create_subject(
            code="MATH",
            name="Mathematics",
        )

        self.grade_id = self.create_grade(
            subject_id=self.subject_id,
            code="G10",
            name="Grade 10",
        )

    # ==========================================================
    # CREATE
    # ==========================================================

    def test_create_success(self):

        chapter = Chapter(
            grade_id=self.grade_id,
            code="CH01",
            name="Functions",
            description="Linear Functions",
            sort_order=1,
        )

        chapter_id = self.repo.create(chapter)

        self.assertGreater(chapter_id, 0)

    def test_create_multiple_chapters(self):

        ...

    def test_exists_code_true(self):

        self.create_chapter(
            grade_id=self.grade_id,
            code="CH01",
            name="Functions",
        )

        self.assertTrue(
            self.repo.exists_code(
                self.grade_id,
                "CH01",
            )
        )

    def test_exists_code_false(self):

        self.assertFalse(
            self.repo.exists_code(
                self.grade_id,
                "UNKNOWN",
            )
        )

    def test_get_by_id_found(self):

        chapter_id = self.create_chapter(
            grade_id=self.grade_id,
            code="CH01",
            name="Functions",
        )

        chapter = self.repo.get_by_id(chapter_id)

        self.assertIsNotNone(chapter)
        self.assertEqual(chapter.id, chapter_id)
        self.assertEqual(chapter.code, "CH01")
        self.assertEqual(chapter.name, "Functions")

    def test_get_by_id_not_found(self):

        chapter = self.repo.get_by_id(999999)

        self.assertIsNone(chapter)

    def test_get_by_code_found(self):

        self.create_chapter(
            grade_id=self.grade_id,
            code="CH02",
            name="Quadratic",
        )

        chapter = self.repo.get_by_code(
            self.grade_id,
            "CH02",
        )

        self.assertIsNotNone(chapter)
        self.assertEqual(chapter.code, "CH02")

    def test_get_by_code_not_found(self):

        chapter = self.repo.get_by_code(
            self.grade_id,
            "NONE",
        )

        self.assertIsNone(chapter)

    def test_get_by_grade_returns_all(self):

        self.create_chapter(
            grade_id=self.grade_id,
            code="CH01",
            name="Functions",
            sort_order=1,
        )

        self.create_chapter(
            grade_id=self.grade_id,
            code="CH02",
            name="Quadratic",
            sort_order=2,
        )

        chapters = self.repo.get_by_grade(self.grade_id)

        self.assertEqual(len(chapters), 2)
        self.assertEqual(chapters[0].code, "CH01")
        self.assertEqual(chapters[1].code, "CH02")

    def test_get_by_grade_empty(self):

        chapters = self.repo.get_by_grade(self.grade_id)

        self.assertEqual(chapters, [])

    def test_get_active_by_grade(self):

        self.create_chapter(
            grade_id=self.grade_id,
            code="CH01",
            status=1,
        )

        self.create_chapter(
            grade_id=self.grade_id,
            code="CH02",
            status=1,
        )

        chapters = self.repo.get_active_by_grade(self.grade_id)

        self.assertEqual(len(chapters), 2)

    def test_deleted_chapter_not_returned(self):

        chapter_id = self.create_chapter(
            grade_id=self.grade_id,
            code="CH01",
            status=1,
        )

        self.repo.delete(chapter_id)

        chapters = self.repo.get_active_by_grade(self.grade_id)

        self.assertEqual(len(chapters), 0)

    def test_search_by_code(self):

        self.create_chapter(
            grade_id=self.grade_id,
            code="CH01",
            name="Functions",
        )

        result = self.repo.search("CH01")

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].code, "CH01")

    def test_search_by_name(self):

        self.create_chapter(
            grade_id=self.grade_id,
            code="CH01",
            name="Functions",
        )

        result = self.repo.search("Function")

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Functions")

    def test_search_no_result(self):

        self.create_chapter(
            grade_id=self.grade_id,
            code="CH01",
            name="Functions",
        )

        result = self.repo.search("Geometry")

        self.assertEqual(result, [])

    def test_update_success(self):

        chapter_id = self.create_chapter(
            grade_id=self.grade_id,
            code="CH01",
            name="Functions",
        )

        chapter = self.repo.get_by_id(chapter_id)

        chapter.name = "Updated Functions"

        self.assertTrue(self.repo.update(chapter))

        updated = self.repo.get_by_id(chapter_id)

        self.assertEqual(updated.name, "Updated Functions")

    def test_update_invalid_id(self):

        chapter = self.repo.get_by_id(9999)

        self.assertIsNone(chapter)

    def test_delete_soft_delete(self):

        chapter_id = self.create_chapter(
            grade_id=self.grade_id,
            code="CH01",
        )

        self.assertTrue(self.repo.delete(chapter_id))

        chapter = self.repo.get_by_id(chapter_id)

        self.assertEqual(chapter.status, 0)

    def test_delete_invalid_id(self):

        self.assertFalse(self.repo.delete(9999))

    def test_restore_success(self):

        chapter_id = self.create_chapter(
            grade_id=self.grade_id,
            code="CH01",
        )

        self.repo.delete(chapter_id)

        self.assertTrue(self.repo.restore(chapter_id))

        chapter = self.repo.get_by_id(chapter_id)

        self.assertEqual(chapter.status, 1)

    def test_restore_invalid_id(self):

        self.assertFalse(self.repo.restore(9999))

    def test_repository_can_be_created(self):

        repo = ChapterRepository(self.conn)

        self.assertIsNotNone(repo)