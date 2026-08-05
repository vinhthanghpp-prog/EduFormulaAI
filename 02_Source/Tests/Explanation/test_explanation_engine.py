import unittest

from Explanation.engine import ExplanationEngine


class TestExplanationEngine(unittest.TestCase):

    def test_engine_can_be_created(self):
        engine = ExplanationEngine()

        self.assertIsNotNone(engine)

    def test_engine_has_generate(self):
        engine = ExplanationEngine()

        self.assertTrue(hasattr(engine, "generate"))

    def test_generate_accepts_learning_content_parameter(self):
        engine = ExplanationEngine()

        self.assertEqual(
            engine.generate.__code__.co_argcount,
            2,
        )

    def test_generate_returns_result(self):
        engine = ExplanationEngine()

        result = engine.generate(None)

        self.assertIsNotNone(result)


if __name__ == "__main__":
    unittest.main()