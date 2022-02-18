import unittest
from typing import List

"""
Дан список some_list требуется написать метод, 
проверяющий, что все члены списка – принадлежат типу int и вывести результат True\False.
"""


def check_type_of_elements(input_value: List) -> bool:
    if not isinstance(input_value, list):
        raise TypeError("Parameter should be type of List")
    elif len(input_value) == 0:
        raise ValueError("Parameter should not be empty.")

    return all(type(x) is int for x in input_value)


class TestListElements(unittest.TestCase):

    def test_all_elements_are_integers(self):
        test_input = [1, 2, 3, 4, 5]

        self.assertTrue(check_type_of_elements(test_input))


if __name__ == '__main__':
    unittest.main(verbosity=2)


