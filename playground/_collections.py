from collections import OrderedDict, ChainMap, Counter, defaultdict


counter = Counter("hello") # counts elements of sequence
print(counter)
counter.update("word")
print(counter)

print(counter.most_common(3))

dd = defaultdict(int)
print(dd["ergergq"])
for char in "hello":
    dd[char] += 1
print(dd)
