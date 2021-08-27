"""
pop() выкидывает последний элемент по дефолту
pop(0) - выкидывает первый и тд.
"""
my_list = ['a', 'b', 'c', 'd']
print(my_list)
popped_last = my_list.pop()
print(my_list)
print(popped_last)

my_list2 = ['a', 'b', 'c', 'd']
print(my_list2)
popped_first = my_list2.pop(0)
print(my_list2)
print(popped_first)