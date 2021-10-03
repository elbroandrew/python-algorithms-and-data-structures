def new_decorator(func):

    def wrap_func():
        print("some code before executing func")
        func()
        print("some code after executing func")

    return wrap_func


if __name__ == '__main__':
    x = hello()
    print(x())
