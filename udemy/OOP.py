class NameOfClass:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def some_method(self):
        print(self.param1)


if __name__ == '__main__':
    o = NameOfClass('hello', 'world')
    o.some_method()
