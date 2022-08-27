import unittest
from src.reverse_polish_notation_evaluator.arithmetic_evaluator import evaluate


class TestArithmeticEvaluator(unittest.TestCase):
    def test_single_operator_expression(self):
        self.assertEqual(evaluate(["3"]), 3)

    def test_simple_operator_expression(self):
        self.assertEqual(evaluate(["2", "5", "*", "4", "+", "3", "2", "*", "1", "+", "/"]), 2)
