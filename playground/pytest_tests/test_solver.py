from unittest import TestCase
from solver import add, square_equation_solver


class TestAddCase(TestCase):
    def test_ok(self):
        result = add(1, 2)
        self.assertEqual(3, result)


class TestSquareEquationSolver(TestCase):
    def test_raises_type_error(self):
        with self.assertRaises(TypeError):
            square_equation_solver("", 1, 1.5)

