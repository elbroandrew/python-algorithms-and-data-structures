class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, target):
        return Number(self.value + target.value)


a = Number(5)
b = Number(3)
print((a + b).value)
