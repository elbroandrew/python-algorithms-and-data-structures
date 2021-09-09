from unittest import TestCase
import pytest
from solver import add, square_equation_solver


def test_add():
    result = add(1, 2)
    assert result == 3


class TestSquareEquationSolverUnittest(TestCase):
    def test_raises_type_error(self):
        with self.assertRaises(TypeError):
            square_equation_solver("", 1, 1.5)

    def test_result_is_tuple(self):
        res = square_equation_solver(0,0,0)
        self.assertIsInstance(res, tuple)

    def test_no_results(self):
        res = square_equation_solver(0,0,1)
        self.assertEqual(res, (None, None))

    def test_resolves_ok(self):
        res = square_equation_solver(1, -3, -4)
        self.assertEqual(res, (4, -1))


class TestSquareEquationSolver():
    def test_raises_type_error(self):
        with pytest.raises(TypeError):
            square_equation_solver("", 1, 1.5)