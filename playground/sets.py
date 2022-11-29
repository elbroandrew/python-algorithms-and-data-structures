my_set = set()
my_set.add(1)
my_set.add(1)
my_set.add(1)
my_set.add(1)
my_set.add(2)
my_set.add(2)
my_set.add(2)
my_set.add(4)
my_set.add(4)
my_set.add(4)
print(my_set)
'''
можно передать лист
'''
my_list = [1,1,1,1,2,3,4,5,5,5,5,5,5,5]
another_set = set(my_list)
print(another_set)

"""
Сет не может содержать мутабельные типы данных.
"""
a = 5 # immutable
b = "test"  # immutable
c = [1,2,3] # mutable or UNhashable

# s = set([a, b, c]) # error for 'c' ---> TypeError: unhashable type: 'list'
# print(s)
#print(hash(c)) # same error
