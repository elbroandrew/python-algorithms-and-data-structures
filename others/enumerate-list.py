a = [34, 65,23 ,87,356,97,45,76,66]

for i in enumerate(a):
    print(i)

"""
возвращет кортежи (index, element)
(0, 34)
(1, 65)
(2, 23)
...
"""
for i, x in enumerate(a):
    print(x, i)

# можно задать стартовый индекс
seasons = ["Summer", "Winter", "Fall", "Spring"]

for count, season in enumerate(seasons, start=1):
    print("{} - {}".format(count, season))
