from functools import wraps
from typing import Callable

# task 1
"""
for 10 returns => 2, 4, 6, 8, 10
"""


def invert(func: Callable):
    @wraps(func)
    def wrapper(x: int):
        res: list = func(x)
        try:
            if isinstance(res, list):
                if x <= 0:
                    res = [*map(abs, res)]
                else:
                    res = [-x for x in res]

        except RuntimeError:
            print("RESULT IS NOT LIST.")
        return res
    return wrapper


@invert
def foo(seq: int = 10) -> list:
    step = 1
    if seq < 0:
        step = -1

    return [x for x in range(0, seq, step) if abs(x) % 2 == 0 and x != 0]


def test() -> None:
    try:
        assert foo(-10) == [2, 4, 6, 8]
        assert foo(10) == [-2, -4, -6, -8]
        print("TESTS PASSED.")
    except AssertionError:
        print("!! TESTS FAILED.")


test()
