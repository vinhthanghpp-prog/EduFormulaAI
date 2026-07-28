from Services.chapter_service import ChapterService

from Tests.test_base import RepositoryTestCase

from Database.Repository.chapter_repository import ChapterRepository


class TestChapterService(RepositoryTestCase):

    def setUp(self):

        super().setUp()

        self.service = ChapterService(
            ChapterRepository(self.conn)
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

    def test_service_can_be_created(self):

        self.assertIsNotNone(self.service)

    def test_create_success(self):

        chapter = self.service.create_chapter(
            grade_id=self.grade_id,
            code="CH01",
            name="Functions",
            description="Functions chapter",
            sort_order=1,
        )

        self.assertIsNotNone(chapter)
        self.assertEqual(chapter.code, "CH01")
        self.assertEqual(chapter.name, "Functions")

    def test_duplicate_code(self):

        self.service.create_chapter(
            grade_id=self.grade_id,
            code="CH01",
            name="Functions",
        )

        with self.assertRaises(ValueError):

            self.service.create_chapter(
                grade_id=self.grade_id,
                code="CH01",
                name="Another Chapter",
            )

    def test_empty_code(self):

        with self.assertRaises(ValueError):

            self.service.create_chapter(
                grade_id=self.grade_id,
                code="",
                name="Functions",
            )

    def test_empty_name(self):

        with self.assertRaises(ValueError):

            self.service.create_chapter(
                grade_id=self.grade_id,
                code="CH01",
                name="",
            )

    def test_invalid_grade(self):

        with self.assertRaises(ValueError):

            self.service.create_chapter(
                grade_id=9999,
                code="CH01",
                name="Functions",
            )