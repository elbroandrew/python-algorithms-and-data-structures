def iterative_fib(n):
    result = [0, 1]
    for i in range(2, n + 1):
        prev1 = result[i - 1]
        prev2 = result[i - 2]
        result.append(prev1 + prev2)
    
    return result[n]


res = iterative_fib(7)
print(res)
