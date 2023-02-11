import timeit

nums = [1,2,3,4,5]
powers = [2,3,4]

res = timeit.timeit(
    "list(map(lambda x, y: x ** y, nums, powers))",
    globals={
        "nums": nums,
        "powers": powers
    }
)

print(res)

def power_num(n, p):
    return n**p

res2 = timeit.timeit(
    "list(map(power_num, nums, powers))",
    globals={
        "nums": nums,
        "powers": powers,
        "power_num": power_num
    }
)

print(res2)

