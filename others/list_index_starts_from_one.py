'''
есть такой дандер метод __getitem__(self)
'''

# список значений двойки в степени
list1 = [2**i for i in range(1, 5)]

print(list1)

# создам класс, где поменяю индекс начала с 0 на 1

class MyList():
    def __init__(self, my_list):
        self.my_list = my_list

    def __getitem__(self, key):
        if key > 0:
            return self.my_list[key - 1]
        else:
            raise IndexError("Out of bounds")

m = MyList(list1)
print(m[5])