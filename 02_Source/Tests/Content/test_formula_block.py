import unittest

from Content.blocks import FormulaBlock


class TestFormulaBlock(unittest.TestCase):

    def test_formula_block_can_be_created(self):
        block = FormulaBlock()

        self.assertIsNotNone(block)