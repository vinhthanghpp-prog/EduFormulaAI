import unittest

from Database.Repository.lesson_repository import LessonRepository
from Database.models import Lesson

from Tests.test_base import RepositoryTestCase

class TestLessonRepository(RepositoryTestCase):
    def setUp(self):

        super().setUp()

        self.repository = LessonRepository(self.conn)

        self.subject_id = self.create_subject(
            code="MATH",
            name="Mathematics",
        )

        self.grade_id = self.create_grade(
            subject_id=self.subject_id,
            code="G10",
            name="Grade 10",
        )

        self.chapter_id = self.create_chapter(
            grade_id=self.grade_id,
            code="CH01",
            name="Functions",
        )

    def test_repository_can_be_created(self):

        self.assertIsNotNone(self.repository)

    def test_create_success(self):

        lesson = Lesson(
            chapter_id=self.chapter_id,
            code="L01",
            name="Introduction",
            description="",
            learning_time=45,
            sort_order=1,
            status=1,
        )

        lesson_id = self.repository.create(lesson)

        self.assertGreater(lesson_id, 0)

    def test_get_by_id(self):

        lesson = Lesson(
            chapter_id=self.chapter_id,
            code="L01",
            name="Introduction",
        )

        lesson_id = self.repository.create(lesson)

        result = self.repository.get_by_id(lesson_id)

        self.assertIsNotNone(result)

        self.assertEqual("L01", result.code)

        self.assertEqual("Introduction", result.name)

    def test_get_by_id_not_found(self):

        self.assertIsNone(
            self.repository.get_by_id(9999)
        )

    def test_exists_code(self):

        lesson = Lesson(
            chapter_id=self.chapter_id,
            code="L01",
            name="Introduction",
        )

        self.repository.create(lesson)

        self.assertTrue(
            self.repository.exists_code(
                self.chapter_id,
                "L01",
            )
        )

        self.assertFalse(
            self.repository.exists_code(
                self.chapter_id,
                "L99",
            )
        )

    def test_get_by_chapter(self):

        self.repository.create(
            Lesson(
                chapter_id=self.chapter_id,
                code="L01",
                name="Lesson 1",
            )
        )

        self.repository.create(
            Lesson(
                chapter_id=self.chapter_id,
                code="L02",
                name="Lesson 2",
            )
        )

        lessons = self.repository.get_by_chapter(
            self.chapter_id
        )

        self.assertEqual(2, len(lessons))

    def test_update_success(self):

        lesson = Lesson(
            chapter_id=self.chapter_id,
            code="L01",
            name="Old Name",
        )

        lesson.id = self.repository.create(lesson)

        lesson.name = "New Name"

        self.assertTrue(
            self.repository.update(lesson)
        )

        updated = self.repository.get_by_id(
            lesson.id
        )

        self.assertEqual(
            "New Name",
            updated.name,
        )

    def test_delete_success(self):

        lesson = Lesson(
            chapter_id=self.chapter_id,
            code="L01",
            name="Lesson",
        )

        lesson_id = self.repository.create(lesson)

        self.assertTrue(
            self.repository.delete(lesson_id)
        )

        self.assertIsNone(
            self.repository.get_by_id(lesson_id)
        )