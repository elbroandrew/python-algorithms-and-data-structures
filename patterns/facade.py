"""
работаем с фасадом, за которым много объектов скрывается
"""


class ElementA:

    def print_hello(self):
        print("HELLO")


class ElementB:

    def print_world(self):
        print("WORLD")


class Facade:

    def __init__(self):
        self.element_A = ElementA()
        self.element_B = ElementB()

    def hello_world(self):
        self.element_A.print_hello()
        self.element_B.print_world()


def main():
    facade: Facade = Facade()
    facade.hello_world()


if __name__ == '__main__':
    main()
