import unittest

from Database.Repository.knowledge_repository import KnowledgeRepository
from Services.knowledge_service import KnowledgeService

from Tests.test_base import RepositoryTestCase


class TestKnowledgeService(RepositoryTestCase):

    def setUp(self):

        super().setUp()

        self.service = KnowledgeService(
            KnowledgeRepository(self.conn)
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

        self.lesson_id = self.create_lesson(
            chapter_id=self.chapter_id,
            code="L01",
            name="Introduction",
        )

    def test_service_can_be_created(self):

        self.assertIsNotNone(self.service)

    def test_create_success(self):

        knowledge = self.service.create_knowledge(
            lesson_id=self.lesson_id,
            code="KN01",
            title="Definition",
            knowledge_type="concept",
        )

        self.assertEqual("KN01", knowledge.code)

        self.assertEqual("Definition", knowledge.title)

    def test_empty_code(self):

        with self.assertRaises(ValueError):

            self.service.create_knowledge(
                lesson_id=self.lesson_id,
                code="",
                title="Definition",
                knowledge_type="concept",
            )

    def test_empty_title(self):

        with self.assertRaises(ValueError):

            self.service.create_knowledge(
                lesson_id=self.lesson_id,
                code="KN01",
                title="",
                knowledge_type="concept",
            )

    def test_invalid_lesson(self):

        with self.assertRaises(ValueError):

            self.service.create_knowledge(
                lesson_id=9999,
                code="KN01",
                title="Definition",
                knowledge_type="concept",
            )

    def test_duplicate_code(self):

        self.service.create_knowledge(
            lesson_id=self.lesson_id,
            code="KN01",
            title="Definition",
            knowledge_type="concept",
        )

        with self.assertRaises(ValueError):

            self.service.create_knowledge(
                lesson_id=self.lesson_id,
                code="KN01",
                title="Another",
                knowledge_type="concept",
            )