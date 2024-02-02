
from collections import OrderedDict

first = OrderedDict({1: 1, 2: 2})

print(first)
print(first.popitem(last=False))  # print first element

d2 = OrderedDict({'a':1, 'b':2, 'c':3})
d2.move_to_end('c', last=False) # OrderedDict([('c', 3), ('a', 1),('b', 2)])

print(d2)


