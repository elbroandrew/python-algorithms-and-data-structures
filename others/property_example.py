class Accum:
    def __init__(self):
        self._count = 0

    @property
    def count(self):
        return self._count

    def add(self, val=1):
        self._count += val


a = Accum()
print(a.count)
a.add()
print(a.count)
