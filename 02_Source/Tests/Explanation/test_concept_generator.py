import unittest

from Explanation.concept_generator import ConceptGenerator


class TestConceptGenerator(unittest.TestCase):

    def test_generator_can_be_created(self):
        generator = ConceptGenerator()

        self.assertIsNotNone(generator)

    def test_generator_has_generate(self):
        generator = ConceptGenerator()

        self.assertTrue(
            hasattr(generator, "generate")
        )

    def test_generate_accepts_content_parameter(self):
        generator = ConceptGenerator()

        self.assertEqual(
            generator.generate.__code__.co_argcount,
            2,
        )

    def test_generate_returns_string(self):
        generator = ConceptGenerator()

        result = generator.generate(None)

        self.assertIsInstance(
            result,
            str,
        )