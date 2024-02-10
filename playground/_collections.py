from collections import namedtuple
import csv

Cat = namedtuple('Cat', "name age color")
tom = Cat('Tom', 4, 'black')
print(tom)

# POINT = namedtuple("POINT", "x y")

# with open('points.csv') as file:
#     for line in csv.reader(file):
#         point = POINT._make(line)
#         print(point)


# быстрое изменение полей
tom = tom._replace(age=1)  ## Cat(name='Tom', age=1, color='black')
print(tom)
# сделать всю структуру изменяемой
tom = tom._asdict()
print(type(tom))   ##  -> OrderedDict

# переименовывание: если попадаются зарезервированные слова или дубликаты
headers = ("name", "age", "with")
# Pet = namedtuple("Pet", headers)  ## ошибка, т.к. 'with' зарезервированно
Pet = namedtuple("Pet", headers, rename=True)  # ошибки нет
