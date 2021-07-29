def recursive_fib(n):
    # base case
    if n < 2:
        return n

    return recursive_fib(n - 2) + recursive_fib(n - 1)


end = 7
for k in range(0, end + 1):
    print(recursive_fib(k))