# tail recursion
# when the recursive call is the last thing done by the function

def fun(n: int):
    if n == 0:
        return
    else:
        print(n)

    return fun(n-1)

# output for fun(3) is: 3 2 1 



# non tail recursion
def fun2(n: int):
    if n == 0:
        return
    fun2(n-1)
    print(n)
# output for fun2(3) is: 1 2 3


def factorial_with_tail_recursion(n: int):

    def loop(x: int, accumulator: int):
        if x <= 1:
            return accumulator
        else:
            return loop(x-1, x*accumulator)
    
    return loop(n, 1)

#print(factorial_with_tail_recursion(30))

# factorial non tail recursion
def fact(n: int) -> int:
    if n <= 0:
        return 1
    else:
        return n * fact(n - 1)

print(fact(100))
