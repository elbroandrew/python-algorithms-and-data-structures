# tail recursion
# when the recursive call is the last thing done by the function

def fun(n: int):
    if n == 0:
        return
    else:
        print(n)

    return fun(n-1)



if __name__ == "__main__":
    fun(5)