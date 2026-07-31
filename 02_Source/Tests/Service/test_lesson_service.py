import unittest

from Database.Repository.lesson_repository import LessonRepository
from Database.Repository.chapter_repository import ChapterRepository
from Services.lesson_service import LessonService

from Tests.test_base import RepositoryTestCase


class TestLessonService(RepositoryTestCase):

    def setUp(self):

        super().setUp()

        self.service = LessonService(
            LessonRepository(self.conn)
        )

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

    def test_service_can_be_created(self):

        self.assertIsNotNone(self.service)

    def test_create_success(self):

        lesson = self.service.create_lesson(
            chapter_id=self.chapter_id,
            code="L01",
            name="Introduction",
        )

        self.assertEqual("L01", lesson.code)

        self.assertEqual("Introduction", lesson.name)

    def test_empty_code(self):

        with self.assertRaises(ValueError):

            self.service.create_lesson(
                chapter_id=self.chapter_id,
                code="",
                name="Lesson",
            )

    def test_empty_name(self):

        with self.assertRaises(ValueError):

            self.service.create_lesson(
                chapter_id=self.chapter_id,
                code="L01",
                name="",
            )

    def test_invalid_chapter(self):

        with self.assertRaises(ValueError):

            self.service.create_lesson(
                chapter_id=9999,
                code="L01",
                name="Lesson",
            )

    def test_duplicate_code(self):

        self.service.create_lesson(
            chapter_id=self.chapter_id,
            code="L01",
            name="Lesson 1",
        )

        with self.assertRaises(ValueError):

            self.service.create_lesson(
                chapter_id=self.chapter_id,
                code="L01",
                name="Lesson 2",
            )