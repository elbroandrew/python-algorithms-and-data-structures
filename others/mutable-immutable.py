"""immutable
None
int
float
str
bool
tuple
"""
"""mutable
list
dict
set
"""
# x = 1
# print(id(x))
# x = 5
# print(id(x))

# s = "кот" # набор символов есть строка
# # s[-1] = 'д' # нельзя
# s1 = s
# print(id(s))
# print(id(s1)) # ссылаются на один объект
# print(s is s1)
# s += '!' # пересоздали переменную
# print(id(s))

# неявное изменение
y = [1, 2, 3]
print(id(y))
def change(var):
    var[0] += 1 # это плохой стиль, тут надо сделать return
    return y

y = change(y) # и здесь присвоить к той же переменной
print(id(y)) # id те же остались
