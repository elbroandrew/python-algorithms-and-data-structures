# task 1
"""
for 10 returns => 2, 4, 6, 8, 10
"""


def foo(seq: int = 10) -> list:
    step = 1
    if seq < 0:
        step = -1

    return [x for x in range(0, seq, step) if abs(x) % 2 == 0]


def test() -> None:
    try:
        assert foo(-10) == [0, -2, -4, -6, -8]
        assert foo(10) == [0, 2,4,6,8]
        print("TESTS PASSED.")
    except AssertionError:
        print("!! TESTS FAILED.")


test()
