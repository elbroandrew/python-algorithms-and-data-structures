def fib(n, memo: dict = None):
    if not memo:
        memo = {}
    if n in memo.keys():
        return memo[n]
    if n <= 2:
        return 1
    res = fib(n-1, memo) + fib(n-2, memo)
    memo[n] = res
    return res


print(fib(7))

if __name__ == "__main__":
    assert fib(7) == 13
    assert fib(8) == 21
    


    
    