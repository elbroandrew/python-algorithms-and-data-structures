def iterative_fib(n):
    result = [0, 1]
    for i in range(2, n + 1):
        prev1 = result[i - 1]
        prev2 = result[i - 2]
        result.append(prev1 + prev2)
    
    return result[n]


res = iterative_fib(7)
print(res)


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

test = fib_without_array(7)
print(test)