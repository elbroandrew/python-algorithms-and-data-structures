# tail recursion -- не существует в питоне
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

fun2(3000)