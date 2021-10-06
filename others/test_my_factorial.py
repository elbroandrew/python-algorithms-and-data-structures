from my_factorial import factorial


def test_factorial():
    cases = [
        (0, 1),
        (4, 24),
        (5, 120),
    ]

    for input_number, output in cases:
        assert factorial(input_number) == output

