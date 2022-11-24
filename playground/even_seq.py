# task 1
"""
for 10 returns => 2, 4, 6, 8, 10
"""


def foo(seq: int = 10):
    step = 1
    if seq < 0:
        step = -1

    print(*[x for x in range(0, seq, step) if x % 2 <= 0])


foo(-10)
foo(10)
