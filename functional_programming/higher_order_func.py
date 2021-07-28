'''
ф-ии, кот-ые примнимают в качестве аргумента другие ф-ии или возвращают.
'''

def f(x):
    return x * 3


def g(func, x):
    return func(x) + func(x)

print(g(f, 5))
