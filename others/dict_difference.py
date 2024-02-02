'''
найти все числа во втором списке, которых нет в первом
'''


def my_method(l1: list, l2: list):
  for n in l1:
    if n in l2:
      l2.remove(n)
    else:
      continue
    
  return l2


res = my_method([1,1,2,3,4, 6], [1, 1, 2, 12, 1, 6, 6, 7, 8]) # [1, 12, 6, 7, 8]
res.sort()
print(res)
