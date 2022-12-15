'''
Напишите класс Point3D для хранения координат в трехмерном пространстве (x, y, z).
Реализуйте перегрузку операторов сложения, вычитания, умножения и деления для этого класса.
Также сделайте возможность сравнения координат между собой и запись/считывание значений через ключи: “x”, “y”, “z”.
'''


class Point3D:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Point3D(x={self.x}, y={self.y}, z={self.z})"

    def __add__(self, other):
        if not isinstance(other, Point3D):
            raise AttributeError("You can sum up only Point3D objects.")

        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z

        return Point3D(x, y, z)




p1 = Point3D(-10, 15, -5)
p2 = Point3D(10, 15, -5)
p3 = p1 + p2

print(p1)
print(p2)
print(p3)