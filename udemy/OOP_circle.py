class Circle:
    pi: float = 3.14 # т.е. это пи может быт использ как self.pi, а так же как Class.pi

    def __init__(self, radius):
        self.radius = radius

    def area(self) -> float:
        return self.radius * self.pi


if __name__ == '__main__':
    c = Circle(20)
    print(c.area())
    print(Circle.pi)
