def new_decorator(func):

    def wrap_func():
        print("some code before executing func")
        func()
        print("some code after executing func")

    return wrap_func


@new_decorator # то же, что и  func_needs_decorator = new_decorator(func_needs_decorator)
def func_needs_decorator():
    print("decorate me")


if __name__ == '__main__':
    func_needs_decorator()
