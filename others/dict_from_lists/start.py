from typing import List
import unittest
from itertools import zip_longest

"""Есть два списка разной длины. В первом содержатся ключи, а во втором значения. 
Напишите функцию, которая создаёт из этих ключей и значений словарь. 
Если ключу не хватило значения, в словаре должно быть значение None. 
Значения, которым не хватило ключей, нужно игнорировать."""


def dict_from_keys_and_values(list1: List, list2: List) -> dict:

    return dict(zip(list1, list2)) if (len(list1) <= len(list2)) else dict(zip_longest(list1, list2))


class CreateDict(unittest.TestCase):

    def test_len_keys_equal_values(self):
        keys = ['one', 'two', 'three']
        values = [1, 2, 3]
        result = dict(one=1, two=2, three=3)

        self.assertEqual(dict_from_keys_and_values(keys, values), result)

    def test_len_keys_gt_values(self):
        keys = ['one', 'two', 'three', 'four']
        values = [1, 2, 3]
        result = dict(one=1, two=2, three=3, four=None)

        self.assertEqual(dict_from_keys_and_values(keys, values), result)




if __name__ == '__main__':
    unittest.main()
