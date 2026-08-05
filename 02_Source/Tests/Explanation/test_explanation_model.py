import unittest

from Explanation.engine import ExplanationEngine


class TestExplanationModel(unittest.TestCase):

    def test_explanation_can_be_created(self):
        explanation = Explanation()

        self.assertIsNotNone(explanation)

    def test_explanation_has_title(self):
        explanation = Explanation()

        self.assertEqual(
            explanation.title,
            "",
        )

    def test_explanation_has_summary(self):
        explanation = Explanation()

        self.assertEqual(
            explanation.summary,
            "",
        )

    def test_explanation_has_concept(self):
        explanation = Explanation()

        self.assertEqual(
            explanation.concept,
            "",
        )

    def test_explanation_has_formula_explanation(self):
        explanation = Explanation()

        self.assertEqual(
            explanation.formula_explanation,
            "",
        )

    def test_explanation_has_variable_explanation(self):
        explanation = Explanation()

        self.assertEqual(
            explanation.variable_explanation,
            "",
        )

    def test_explanation_has_empty_steps(self):
        explanation = Explanation()

        self.assertEqual(
            explanation.steps,
            [],
        )

    def test_explanation_has_empty_examples(self):
        explanation = Explanation()

        self.assertEqual(
            explanation.examples,
            [],
        )

    def test_explanation_has_empty_tips(self):
        explanation = Explanation()

        self.assertEqual(
            explanation.tips,
            [],
        )

    def test_explanation_has_empty_common_mistakes(self):
        explanation = Explanation()

        self.assertEqual(
            explanation.common_mistakes,
            [],
        )

    def test_explanation_has_empty_learning_notes(self):
        explanation = Explanation()

        self.assertEqual(
            explanation.learning_notes,
            [],
        )


if __name__ == "__main__":
    unittest.main()