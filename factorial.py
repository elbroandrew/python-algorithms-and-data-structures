def factorial(number: int) -> int:
    result = 1
    for i in range(1, number+1):
        result *= i

    return result


if __name__ == '__main__':
    cases = [
        (0, 1),
        (4, 24),
        (5, 120),
    ]

    for input_number, output in cases:
        assert factorial(input_number) == output

