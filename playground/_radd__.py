class MyCounter:
    
    def __init__(self, count) -> None:
        self.count = count
        
    def __add__(self, other):
        if isinstance(other, int):
            return MyCounter(self.count + other)
        
        return MyCounter(self.count + other.count)
        
    def __radd__(self, other):
        return self + other
    
    

c1 = MyCounter(5)
c2 = MyCounter(6)
print( (1 + c2).count )