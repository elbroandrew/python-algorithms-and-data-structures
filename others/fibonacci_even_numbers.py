import unittest


def fib_even_numbers(n: int):
    # base case
    if n <= 0:
        raise ValueError("Parameter should be greater than 0")
    elif type(n) is not int:
        raise TypeError("Parameter should be type of 'int'")

    result = []

    def fib():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    x = fib()
    while n > 0:
        z = next(x)
        if z % 2 == 0:
            result.append(z)
            n -= 1

    return result


class TestFibEvenNumbers(unittest.TestCase):

    def test_value_error_raise(self):
        values = [-1, 0]
        for i in values:
            self.assertRaises(ValueError, fib_even_numbers, i)

    def test_type_error_raise(self):
        values = ["string", [1, 2, 3], {}]
        for i in values:
            self.assertRaises(TypeError, fib_even_numbers, i)

    def test_even_numbers(self):
        result = [0, 2, 8, 34]
        count = 4

        self.assertListEqual(fib_even_numbers(count), result)


if __name__ == '__main__':
    unittest.main(verbosity=2)

