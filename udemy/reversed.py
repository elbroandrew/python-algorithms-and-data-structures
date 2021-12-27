'''returns reversed ITERATOR'''

data = ''.join((reversed('hello')))
print(data)

# second solution
print('hello'[::-1])


# 3 example
for i in reversed(range(0,5)):
    print(i)