from collections import OrderedDict, ChainMap

first = OrderedDict({1: 1, 2: 2})
second = OrderedDict({4: 4, 5: 5})
chain = ChainMap(first, second)
print(chain)
chain[3] = 100
print(chain)


