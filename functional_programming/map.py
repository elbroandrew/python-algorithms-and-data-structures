'''map применяет ф-ию к каждому элементу и возвращает итератор (список)'''

'''arr.map(x => x * 2) в JS'''

arr = [3, 4, 1, 5]

my_list = list(map(lambda x : x * 2, arr))
print(my_list)

'''два списка, суммируем поочереди элементы - первый из первого с первым из второго и тд.'''
list1 = [1,2,3,4,5]
list2 = [10,20,30,40,50]

new_list = list(map(lambda x, y : x + y, list1, list2))
print(new_list)