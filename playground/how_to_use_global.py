a = 10
b = 20
c = 30

def print_globals():
    global c
    print(a, b, c)
    c = 100
    print(c)  # UnboundLocalError: local variable 'c' referenced before assignment (instead of 10, 20, 30)
    # because c = 100 is a new local variable, and we reference it in print(a,b,c)
    # to get 10, 20, 30, just add 'global'

    """
    def print_globals():
        global c  # ref to global 'c'
        print(a, b, c)
        c = 100   # not a local 'c', it will change 'c' to 100
        print(c)  # 100
    """


print_globals()


"keyword 'nonlocal' works for nested functions"


b = 0
def f1():
    b = 1
    def inner():
        nonlocal b  # refers to variable not in outer (not local) space.
        b = 2
        print(b)

    inner()
    print(b)

f1()
