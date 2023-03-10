def find_char(A, n):
    res = 0

    for val in range(1, n + 1): # +1, т.к. n + 1 не входит в range.
        res ^= val

    for val in A:
        res ^= val

    return res


g = [1, 3, 2, 4, 6, 8, 5, 9]  # 7
x = find_char(g, len(g) + 1) # n + 1 т.к. мы ищем в ряду из 10 чисел, а у нас - 10.
print(x)