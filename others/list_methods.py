'''можно создать лист двумя способами'''
list1 = [1,2,3,4]

'''второй для строки'''
mylist = list('Барсик')
print(mylist)

'''4 раза HI'''
hi = ['hi'] * 4
print(hi)

'''slicing'''
# L[2] -- с 0 до 2 элемента
print(list1[2])
# L[-2] с конца
print(list1[-3])
# L[1:]
print(list1[1:])

""" extend list """
list1 = [1,2,3]
list1.extend([4,5])
print(list1)

""" insert """
list1.insert(2, 'Hi!')
print(list1)

""" clear """
list1.clear()
print(list1)

""" pop """
l2 = [1,2,3,4]
x1 = l2.pop(2)
print(x1)

""" remove - удаляет первый найденный элемент, у которого значение X """
l3 = [1,2,3]
l3.remove(3)
print(l3) # удалил цифру 3

""" index позиция элемента """
l4 = [1,2,3,4,5,6,7,8]
print(l4.index(2))
# можно длюавлять с какого индекса искать и по какой даже:
print(l4.index(5, 2))

""" сколько раз N встречается в списке """
l5 = [1,2,2,2,2,3,4,5]
print(l5.count(2))

