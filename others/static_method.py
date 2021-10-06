class Square():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calc_area(self):
        return self.width * self.height
    
    @staticmethod
    def compare_areas(rect1, rect2):
        if rect1 == rect2:
            print("Equal areas.")
        else:
            print("Different areas.")
        
rec1 = Square(6, 2)
rec2 = Square(3, 4)
s1 = rec1.calc_area()
s2 = rec2.calc_area()

Square.compare_areas(s1, s2)
# но так же можно и от объекта получить доступ 
rec1.compare_areas(s1, s2) 


