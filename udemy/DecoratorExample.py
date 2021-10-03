def hello(name="Andrew"):
    print('the hello function has been run')

    def greet():
        return "   This is inside the greet()"

    def welcome():
        return "   This is inside welcome func"

    print(greet())
    print(welcome())


if __name__ == '__main__':
    hello()
