import unittest

from Database.Repository.formula_repository import FormulaRepository
from Database.models import Formula

from Tests.test_base import RepositoryTestCase


class TestFormulaRepository(RepositoryTestCase):

    def setUp(self):

        super().setUp()

        self.repository = FormulaRepository(self.conn)

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

        self.knowledge_id = self.create_knowledge(
            lesson_id=self.lesson_id,
            code="KN01",
            title="Definition",
            knowledge_type="concept",
        )


    def test_repository_can_be_created(self):

        self.assertIsNotNone(self.repository)


    def test_create_success(self):

        formula = Formula(
            knowledge_id=self.knowledge_id,
            code="F01",
            name="Newton Second Law",
            expression="F = m * a",
            description="",
            meaning="",
            conditions="",
            applications="",
            notes="",
            difficulty_level=1,
            sort_order=1,
            status=1,
        )

        formula_id = self.repository.create(formula)

        self.assertGreater(formula_id, 0)


    def test_get_by_id(self):

        formula = Formula(
            knowledge_id=self.knowledge_id,
            code="F01",
            name="Newton Second Law",
            expression="F = m * a",
        )

        formula.id = self.repository.create(formula)

        result = self.repository.get_by_id(formula.id)

        self.assertIsNotNone(result)

        self.assertEqual("F01", result.code)

        self.assertEqual("Newton Second Law", result.name)


    def test_get_by_id_not_found(self):

        self.assertIsNone(
            self.repository.get_by_id(9999)
        )


    def test_exists_code(self):

        formula = Formula(
            knowledge_id=self.knowledge_id,
            code="F01",
            name="Newton",
            expression="F = m * a",
        )

        self.repository.create(formula)

        self.assertTrue(
            self.repository.exists_code(
                self.knowledge_id,
                "F01",
            )
        )

        self.assertFalse(
            self.repository.exists_code(
                self.knowledge_id,
                "F99",
            )
        )


    def test_get_by_knowledge(self):

        self.repository.create(
            Formula(
                knowledge_id=self.knowledge_id,
                code="F01",
                name="Formula 1",
                expression="A",
            )
        )

        self.repository.create(
            Formula(
                knowledge_id=self.knowledge_id,
                code="F02",
                name="Formula 2",
                expression="B",
            )
        )

        items = self.repository.get_by_knowledge(
            self.knowledge_id
        )

        self.assertEqual(2, len(items))


    def test_update_success(self):

        formula = Formula(
            knowledge_id=self.knowledge_id,
            code="F01",
            name="Old Name",
            expression="Old",
        )

        formula.id = self.repository.create(formula)

        formula.name = "New Name"

        self.assertTrue(
            self.repository.update(formula)
        )

        updated = self.repository.get_by_id(
            formula.id
        )

        self.assertEqual(
            "New Name",
            updated.name,
        )


    def test_delete_success(self):

        formula = Formula(
            knowledge_id=self.knowledge_id,
            code="F01",
            name="Formula",
            expression="F=m*a",
        )

        formula.id = self.repository.create(formula)

        self.assertTrue(
            self.repository.delete(formula.id)
        )

        self.assertIsNone(
            self.repository.get_by_id(
                formula.id
            )
        )