from keyword_all import *

"""
при from mymodule import * импортированы будут только те объекты, которые вы описали в __all__
"""

a = A()
b = B() # error
