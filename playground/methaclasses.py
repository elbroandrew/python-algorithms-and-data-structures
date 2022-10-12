"""
классы, которые можно создавать динамически через type()
type('MyClassName', (BaseClass1, BaseClass2,...), {dict of attributes})
"""


def create_class_point(name, bases, attrs):
    attrs.update({'MAX_VALUE': 100, 'MIN_VALUE': 0})
    return type(name, bases, attrs)


class Point(metaclass=create_class_point):
    def get_coords(self):
        return (0, 0)

pt = Point()
print(pt.MAX_VALUE)