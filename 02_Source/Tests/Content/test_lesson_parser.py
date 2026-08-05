import unittest

from Content.parser import ContentParser
from Content.blocks import ConceptBlock
from Content.blocks import FormulaBlock


class TestLessonParser(unittest.TestCase):

    def test_parser_detects_concept_block(self):
        parser = ContentParser()

        source = """
[CONCEPT]
Vector là đại lượng có hướng.
"""

        result = parser.parse(source)

        self.assertEqual(
            len(result),
            1,
        )

        self.assertIsInstance(
            result[0],
            ConceptBlock,
        )

    def test_parser_extracts_concept_content(self):
        parser = ContentParser()

        source = """
    [CONCEPT]
    Vector là đại lượng có hướng.
    """

        result = parser.parse(source)

        self.assertEqual(
            result[0].content,
            "Vector là đại lượng có hướng."
        )

    def test_parser_detects_formula_block(self):
        parser = ContentParser()

        source = """
    [FORMULA]
    F = ma
    """

        result = parser.parse(source)

        self.assertEqual(
            len(result),
            1,
        )

        self.assertIsInstance(
            result[0],
            FormulaBlock,
        )

    def test_parser_extracts_formula_content(self):
        parser = ContentParser()

        source = """
    [FORMULA]
    F = ma
    """

        result = parser.parse(source)

        self.assertEqual(
            result[0].content,
            "F = ma",
        )