class Animal:
    def __init__(self, fur):
        print('Animal created!')

    def report(self):
        print("Animal")

    def woof(self):
        print("woof!")


class Dog(Animal):

    def __init__(self, fur):
        Animal.__init__(self, fur) #creates Animal instance
        print("Dog created")

    def report(self):
        print("Dog")


if __name__ == '__main__':
    dog = Dog("Fur")
    dog.report()
