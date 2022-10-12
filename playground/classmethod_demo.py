"""
привести пример класс метода
"""

"""
@classmethod нужен для логики внутри класса.
"""


class Square:
    MAX_RANGE = 5
    def __init__(self, a):
        self.a = self.check_if_square(a)

    @classmethod
    def check_if_square(cls, x):
        if x <= cls.MAX_RANGE and x > 0:
            return x

        return 1

s = Square(6)
print(s.a)
