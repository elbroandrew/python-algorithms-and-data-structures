import sys

def iterative_fib(n):
    result = [0, 1]
    for i in range(2, n + 1):
        prev1 = result[i - 1]
        prev2 = result[i - 2]
        result.append(prev1 + prev2)
    
    return result[n]


# res = iterative_fib(7)


# iterative w/o an array
def fib_without_array(n):
    a = 0
    b = 1
    c = 0
    if n == 0:
        return 0
    if n == 1:
        return 1
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
    return c

# test = fib_without_array(7)


# fib colt variant  (~500 MB памяти сожрет при 1000000)
def fib_list(max_num):
    nums = []
    a, b = 0, 1
    while len(nums) < max_num:
        nums.append(b)
        a, b = b, a + b
    return nums

# with generator (а тут ~ 5 MB)
def fib_gen(max_num):
    x = 0
    y = 1
    count = 0
    while count < max_num:
        x, y = y, x + y
        yield x
        count += 1

# for n in fib_gen(10):
#     print(n)


if __name__ == "__main__":
    
    # res = sys.getsizeof(iterative_fib(70))   # 32 bytes
    # res = sys.getsizeof(fib_without_array(70))  # 32 bytes
    # res = sys.getsizeof(fib_list(70))  # 664 bytes
    res = sys.getsizeof(x for x in fib_gen(70)) # 112 bytes
    list_comp = sys.getsizeof([x * 10 for x in range(1000)]) # 8856 bytes
    gen_exp = sys.getsizeof(x * 10 for x in range(1000))     # 112 bytes
    print(f"{res} bytes")
