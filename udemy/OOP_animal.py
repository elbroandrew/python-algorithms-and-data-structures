class Animal:
    def __init__(self):
        print('Animal created!')

    def report(self):
        print("Animal")

    def eat(self):
        print("Eating!")


class Dog(Animal):

    def __init__(self):
        print("Dog created")
