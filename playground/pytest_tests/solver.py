def add(a, b):
    return a + b


def square_equation_solver(a, b, c):
    if not all(
        map(
            lambda param: isinstance(param, (int, float)),
            (a, b, c)
        )
    ):
        raise TypeError("Not valid type for param 'a'")
    print("Types are OK")
