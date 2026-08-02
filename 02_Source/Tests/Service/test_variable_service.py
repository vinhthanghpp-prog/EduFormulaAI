import unittest

from Services.variable_service import VariableService
from Database.models import Variable

from Tests.test_base import RepositoryTestCase


class TestVariableService(RepositoryTestCase):

    def setUp(self):

        super().setUp()

        self.service = VariableService(self.conn)

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

    def test_service_can_be_created(self):

        self.assertIsNotNone(self.service)

    def test_create_success(self):

        variable = Variable(
            formula_id=self.formula_id,
            symbol="F",
            name="Force",
        )

        variable_id = self.service.create(variable)

        self.assertGreater(variable_id, 0)

    def test_duplicate_symbol(self):

        self.service.create(
            Variable(
                formula_id=self.formula_id,
                symbol="F",
                name="Force",
            )
        )

        with self.assertRaises(ValueError):

            self.service.create(
                Variable(
                    formula_id=self.formula_id,
                    symbol="F",
                    name="Force 2",
                )
            )

    def test_empty_symbol(self):

        with self.assertRaises(ValueError):

            self.service.create(
                Variable(
                    formula_id=self.formula_id,
                    symbol="",
                    name="Force",
                )
            )

    def test_empty_name(self):

        with self.assertRaises(ValueError):

            self.service.create(
                Variable(
                    formula_id=self.formula_id,
                    symbol="F",
                    name="",
                )
            )

    def test_invalid_formula(self):

        with self.assertRaises(ValueError):

            self.service.create(
                Variable(
                    formula_id=9999,
                    symbol="F",
                    name="Force",
                )
            )