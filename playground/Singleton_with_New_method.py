class Rect:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            return cls.__instance
        else:
            print(f"Instance of class {cls.__name__} already exists.")

    def __del__(self):
        Rect.__instance = None

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.area = a * b

    def get_area(self):
        return "wergeg"


r1 = Rect(2, 3)
r2 = Rect(1, 2)
