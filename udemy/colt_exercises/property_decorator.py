class Mine(object):

    def __init__(self):
        self._x = None

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def del_x(self):
        self._x = None

    x = property(get_x, set_x, del_x, 'Это свойство x.')


type(Mine.x)  # property
mine = Mine()
mine.x()  # None
mine.x = 3
mine.x()  # 3
del mine.x
mine.x()  # None


'''верхний вариант можно заменить ДЕКОРАТОРАМИ'''


class Mine2(object):

    def __init__(self):
        self._x = None

    x = property()

    @x.getter
    def x(self):
        """Это свойство x."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        self._x = None