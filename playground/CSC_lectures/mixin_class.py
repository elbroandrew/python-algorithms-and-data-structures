

class Mixin:
    def increment(self):
        super().increment()
        super().increment()


class B:
    count = 0
    def increment(self):
        self.count += 1


class A(Mixin, B):
    pass


a = A()
print(a.count)
a.increment()
print(a.count)