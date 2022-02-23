import unittest

'''
есть такой дандер метод __getitem__(self)
'''

# список значений двойки в степени
list1 = [2**i for i in range(1, 5)]

print(list1)
print(dir(list1))
# создам класс, где поменяю индекс начала с 0 на 1

class MyList():
    def __init__(self, my_list):
        self.my_list = my_list

    def __getitem__(self, key):
        if key > 0:
            return self.my_list[key - 1]
        elif key < 0:
            return self.my_list[key]
        else:
            raise IndexError("Out of bounds")


class TestMyList(unittest.TestCase):
    def setUp(self) -> None:
        self.list2 = [2 ** i for i in range(1, 5)]
        self.my_list = MyList(self.list2)

    def test_index_zero(self):
        self.assertRaises(IndexError, lambda: self.my_list[0])


if __name__ == '__main__':
    unittest.main(verbosity=2)