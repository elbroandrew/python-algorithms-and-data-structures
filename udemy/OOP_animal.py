class Animal:
    def __init__(self):
        print('Animal created!')

    def report(self):
        print("Animal")

    def woof(self):
        print("woof!")


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self) #creates Animal instance
        print("Dog created")

    def report(self):
        print("Dog")


if __name__ == '__main__':
    dog = Dog()
    dog.report()
