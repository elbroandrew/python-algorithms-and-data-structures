'''
Вывести число в степени 2.
'''

def test(n: int):
    x = n
    while True:
        n *= x
        yield n


gen = test(2)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))