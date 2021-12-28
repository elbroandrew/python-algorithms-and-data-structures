nums = {"one": 1, "two": 2, "three": 3}

# values
for num in nums.values():
    print(num)

# keys
for key in nums.keys():
    print(key)


# keys & values
for item in nums.items():
    print(item)

for k, v in nums.items():
    print(f"k is {k} and value is {v}")


# using 'IN' word
print(2 in nums.values())
print('one' in nums.keys())

'''dictionary methods'''
# CLEAR
d = dict(a=1, b=2, c=3)
#d.clear()
print(d)

#COPY
c = d.copy()
print(c)
print(c is d) # False

#FROMKEYS
x = {}.fromkeys("a", "b")
print(x)
y = {}.fromkeys(['a', 'b', 'c'], 10)
print(y)

#словарь из двух списков с ZIP
keys = ['one', 'two', 'three', 'four']
values = [1,2,3,4]
a = {k: v for k, v in zip(keys, values)}
print(a)

# GET - получает значение по ключу, но не выкидывает KeyError, а None.
print(d['a']) # 1
print(d.get('a')) # 1
#print(d['no_key']) # KeyError
print(d.get('no_key')) # None

'''
-- например, там, где надо узнать сколько раз встречается ключ в словаре.
# имеем список 
lst = [9, 13, 1, 3, 7, 3, 1, 1, 7, 1, 7, 9]
# создаем ключи будущего словаря (множество set() 
# может иметь только уникальные элементы)
key = set(lst)
# создаем словарь `rez` из списка ключей `key` 
# со значением по умолчанию = 0
rez = dict.fromkeys(key, 0)
# {1: 0, 3: 0, 7: 0, 9: 0, 13: 0}

for key in lst:
    # увеличиваем счетчик 
    # соответствующего ключа на 1
    rez[key] += 1

# смотрим результат
print(rez)
{1: 4, 3: 2, 7: 3, 9: 2, 13: 1}
'''


# POP
e = dict(a=1, b=2, c=3)
e.pop('a')
print(e)

# POPITEM - removes RANDOM item
g = dict(a=1, b=2, c=3, d=4, e=5, f=6)
g.popitem()
print(g)

# UPDATE -- можно скопировать словарь в словарь.
first = dict(a=1, b=2, c=3)
second = {}

second.update(first)
print(second)
second['a'] = 5555
print(second)
second.update(first)
print(second)

# DICT COMPREHENSIONS
numbers = dict(first=1, second=2, third=3)
squared_numbers = {key: value ** 2 for key, value in numbers.items()}
print(squared_numbers)

# ex 1
n = {num: num**2 for num in [2,3,4,5]}
print(n)

# ex 2 -- TWO strings into one dictionary
str1 = 'ABC'
str2 = "123"
combo = {str1[i]: str2[i] for i in range(0, len(str1))} # {'A': '1', 'B': '2', 'C': '3'}
print(combo)

# ex 3 -- conditional logic
num_list = [1,2,3,4]
p = {num: "even" if num % 2 == 0 else "odd" for num in num_list}
print(p)
