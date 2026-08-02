import unittest

from Database.Repository.variable_repository import VariableRepository
from Database.models import Variable

from Tests.test_base import RepositoryTestCase


class TestVariableRepository(RepositoryTestCase):

    def setUp(self):

        super().setUp()

        self.repository = VariableRepository(self.conn)

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

        self.formula_id = self.create_formula(
            knowledge_id=self.knowledge_id,
            code="F01",
            name="Newton",
            expression="F = m * a",
        )

    def test_repository_can_be_created(self):

        self.assertIsNotNone(self.repository)

    def test_create_success(self):

        variable = Variable(
            formula_id=self.formula_id,
            symbol="F",
            name="Force",
            unit="N",
        )

        variable_id = self.repository.create(variable)

        self.assertGreater(variable_id, 0)

    def test_get_by_id(self):

        variable = Variable(
            formula_id=self.formula_id,
            symbol="F",
            name="Force",
            unit="N",
        )

        variable.id = self.repository.create(variable)

        result = self.repository.get_by_id(variable.id)

        self.assertEqual(result.symbol, "F")

    def test_get_by_id_not_found(self):

        self.assertIsNone(
            self.repository.get_by_id(9999)
        )

    def test_exists_symbol(self):

        self.repository.create(
            Variable(
                formula_id=self.formula_id,
                symbol="F",
                name="Force",
                unit="N",
            )
        )

        self.assertTrue(
            self.repository.exists_symbol(
                self.formula_id,
                "F",
            )
        )

    def test_get_by_formula(self):

        self.repository.create(
            Variable(
                formula_id=self.formula_id,
                symbol="F",
                name="Force",
            )
        )

        self.repository.create(
            Variable(
                formula_id=self.formula_id,
                symbol="m",
                name="Mass",
            )
        )

        items = self.repository.get_by_formula(
            self.formula_id
        )

        self.assertEqual(len(items), 2)

    def test_update_success(self):

        variable = Variable(
            formula_id=self.formula_id,
            symbol="F",
            name="Force",
        )

        variable.id = self.repository.create(variable)

        variable.name = "Force Updated"

        self.repository.update(variable)

        result = self.repository.get_by_id(variable.id)

        self.assertEqual(
            result.name,
            "Force Updated",
        )

    def test_delete_success(self):

        variable = Variable(
            formula_id=self.formula_id,
            symbol="F",
            name="Force",
        )

        variable.id = self.repository.create(variable)

        self.repository.delete(variable.id)

        self.assertIsNone(
            self.repository.get_by_id(variable.id)
        )