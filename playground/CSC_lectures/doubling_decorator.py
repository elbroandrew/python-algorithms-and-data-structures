import functools

"""
This decrorator replaces an original class method if the class has such method
"""
   
    
def doubling(cls):
    original_increment_method = cls.increment
    def increment(self):
        original_increment_method(self)
        original_increment_method(self)
        
    cls.increment = increment
    return cls


@doubling
class A:
    
    def __init__(self) -> None:
        self.count = 0
        
    def increment(self):
        self.count += 1
    
    
c = A()
print(c.count)
c.increment()
print(c.count)