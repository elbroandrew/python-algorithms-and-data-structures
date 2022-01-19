"""отсортировать словари через sorted"""


names = [
    {"name": "Vasya", "salary": 100},
    {"name": "Masha", "salary": 400},
    {"name": "Petya", "salary": 500},
    {"name": "Kolya", "salary": 200},
    {"name": "Sasha", "salary": 400}]

# sorted может принимать ф-ию, которая будет применена к каждому элементу
# напишу ф-ию
def get_by_salary(var):
    return var['salary']

x = sorted(names, key=get_by_salary)

# print(x)

# можно реверс задать
y = sorted(names, key=get_by_salary, reverse=True)
# print(y)

# example 2
names2 = [
    {"name": "Vasya", "salary": 100, "age": 20},
    {"name": "Masha", "salary": 400, "age": 30},
    {"name": "Petya", "salary": 500, "age": 40},
    {"name": "Kolya", "salary": 200, "age": 70},
    {"name": "Sasha", "salary": 400, "age": 31}]

# сортирнем по двум параметрам
def sort_by_two_params(var):
    return var["salary"], var["age"]

# z = sorted(names2, key=sort_by_two_params)
# print(z)


# через лямбду
f = sorted(names2, key=lambda var: var['salary'])
print(f)

# два параметра в лямбду через тюпл
g = sorted(names2, key=lambda var: (var["salary"], var["age"]))
print(g)

"""
можно импортнуть модуль operator и сделать через itemgetter
sorted(names2, key=operator.itemgetter('salary', 'age'))

"""