import unittest

from Services.formula_service import FormulaService
from Database.models import Formula

from Tests.test_base import RepositoryTestCase


class TestFormulaService(RepositoryTestCase):

    def setUp(self):

        super().setUp()

        self.service = FormulaService(self.conn)

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


    def test_service_can_be_created(self):

        self.assertIsNotNone(self.service)


    def test_create_success(self):

        formula = Formula(
            knowledge_id=self.knowledge_id,
            code="F01",
            name="Newton",
            expression="F = m * a",
        )

        formula_id = self.service.create(formula)

        self.assertGreater(formula_id, 0)


    def test_duplicate_code(self):

        self.service.create(
            Formula(
                knowledge_id=self.knowledge_id,
                code="F01",
                name="Formula 1",
                expression="A",
            )
        )

        with self.assertRaises(ValueError):

            self.service.create(
                Formula(
                    knowledge_id=self.knowledge_id,
                    code="F01",
                    name="Formula 2",
                    expression="B",
                )
            )


    def test_empty_name(self):

        with self.assertRaises(ValueError):

            self.service.create(
                Formula(
                    knowledge_id=self.knowledge_id,
                    code="F01",
                    name="",
                    expression="A",
                )
            )


    def test_empty_expression(self):

        with self.assertRaises(ValueError):

            self.service.create(
                Formula(
                    knowledge_id=self.knowledge_id,
                    code="F01",
                    name="Formula",
                    expression="",
                )
            )


    def test_invalid_knowledge(self):

        with self.assertRaises(ValueError):

            self.service.create(
                Formula(
                    knowledge_id=9999,
                    code="F01",
                    name="Formula",
                    expression="A",
                )
            )