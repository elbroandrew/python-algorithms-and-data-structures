"""
__slots__ НЕ позволяет объекту класса добавлять новые свойства (т.е. он укзывает, что 'будут только эти и никакие другие',
хотя у объектов подкласса от этого класса уже можно менять.
Будет остутствовать метод __dict__
"""


class Car:
    __slots__ = [
        "make",
        "owner",
        "year"
    ]

    def __init__(self, make):
        self.make = make


c1 = Car("nissan")
print(c1.make)

#c1.color = 'red' # error
print(c1.__dict__)
#print(c1.color)
