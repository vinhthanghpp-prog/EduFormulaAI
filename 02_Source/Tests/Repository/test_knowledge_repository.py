import unittest

from Database.Repository.knowledge_repository import KnowledgeRepository
from Database.models import Knowledge

from Tests.test_base import RepositoryTestCase


class TestKnowledgeRepository(RepositoryTestCase):

    def setUp(self):

        super().setUp()

        self.repository = KnowledgeRepository(self.conn)

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


    def test_repository_can_be_created(self):

        self.assertIsNotNone(self.repository)

    def test_create_success(self):

        knowledge = Knowledge(
            lesson_id=self.lesson_id,
            code="KN01",
            title="Definition",
            description="",
            knowledge_type="concept",
            difficulty_level=1,
            sort_order=1,
            status=1,
        )

        knowledge_id = self.repository.create(knowledge)

        self.assertGreater(knowledge_id, 0)

    def test_get_by_id(self):

        knowledge = Knowledge(
            lesson_id=self.lesson_id,
            code="KN01",
            title="Definition",
            knowledge_type="concept",
        )

        knowledge.id = self.repository.create(knowledge)

        result = self.repository.get_by_id(knowledge.id)

        self.assertIsNotNone(result)

        self.assertEqual("KN01", result.code)

        self.assertEqual("Definition", result.title)

    def test_get_by_id_not_found(self):

        self.assertIsNone(
            self.repository.get_by_id(9999)
        )

    def test_exists_code(self):

        knowledge = Knowledge(
            lesson_id=self.lesson_id,
            code="KN01",
            title="Definition",
            knowledge_type="concept",
        )

        self.repository.create(knowledge)

        self.assertTrue(
            self.repository.exists_code(
                self.lesson_id,
                "KN01",
            )
        )

        self.assertFalse(
            self.repository.exists_code(
                self.lesson_id,
                "KN99",
            )
        )

    def test_get_by_lesson(self):

        self.repository.create(
            Knowledge(
                lesson_id=self.lesson_id,
                code="KN01",
                title="Definition",
                knowledge_type="concept",
            )
        )

        self.repository.create(
            Knowledge(
                lesson_id=self.lesson_id,
                code="KN02",
                title="Formula",
                knowledge_type="formula",
            )
        )

        items = self.repository.get_by_lesson(
            self.lesson_id
        )

        self.assertEqual(2, len(items))

    def test_update_success(self):

        knowledge = Knowledge(
            lesson_id=self.lesson_id,
            code="KN01",
            title="Old Title",
            knowledge_type="concept",
        )

        knowledge.id = self.repository.create(knowledge)

        knowledge.title = "New Title"

        self.assertTrue(
            self.repository.update(knowledge)
        )

        updated = self.repository.get_by_id(
            knowledge.id
        )

        self.assertEqual(
            "New Title",
            updated.title,
        )

    def test_delete_success(self):

        knowledge = Knowledge(
            lesson_id=self.lesson_id,
            code="KN01",
            title="Definition",
            knowledge_type="concept",
        )

        knowledge.id = self.repository.create(knowledge)

        self.assertTrue(
            self.repository.delete(knowledge.id)
        )

        self.assertIsNone(
            self.repository.get_by_id(
                knowledge.id
            )
        )