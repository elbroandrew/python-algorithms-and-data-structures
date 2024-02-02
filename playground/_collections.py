from collections import namedtuple
import csv

# Cat = namedtuple('Cat', "name age color")
# tom = Cat('Tom', 4, 'black')
# print(tom)

POINT = namedtuple("POINT", "x y")

with open('points.csv') as file:
    for line in csv.reader(file):
        point = POINT._make(line)
        print(point)



