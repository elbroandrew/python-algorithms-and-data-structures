from unittest import TestCase
from solver import add


class TestAddCase(TestCase):
    def test_ok(self):
        result = add(1, 2)
        self.assertEqual(3, result)
