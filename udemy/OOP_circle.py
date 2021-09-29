class Circle:
    pi: float = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self) -> float:
        return self.radius * self.pi


if __name__ == '__main__':
    c = Circle(20)
    print(c.area())
