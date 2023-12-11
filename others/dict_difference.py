'''
найти все числа во втором списке, которых нет в первом
'''


def my_method(l1: list, l2: list):
  res = {}

  for key in l2:
    if key in res:
      res[key] += 1
    else:
      res[key] = 1

  for key in l1:
    if key in res:
      res[key] -= 1
  print(res)

  for k in res.copy():
    if res[k] == 0:
      del res[k]
    
  return res


res = my_method([1,1,2,3,4, 6], [1, 1, 2, 12, 1, 6, 6, 7, 8]) # 
def my_method(l1: list, l2: list):
  res = {}

  for key in l2:
    if key in res:
      res[key] += 1
    else:
      res[key] = 1

  for key in l1:
    if key in res:
      res[key] -= 1
  print(res)

  for k in res.copy():
    if res[k] == 0:
      del res[k]
    
  return res


res = my_method([1,1,2,3,4, 6], [1, 1, 2, 12, 1, 6, 6, 7, 8]) # 
def my_method(l1: list, l2: list):
  res = {}

  for key in l2:
    if key in res:
      res[key] += 1
    else:
      res[key] = 1

  for key in l1:
    if key in res:
      res[key] -= 1
  print(res)

  for k in res.copy():
    if res[k] == 0:
      del res[k]
    
  return res


res = my_method([1,1,2,3,4, 6], [1, 1, 2, 12, 1, 6, 6, 7, 8]) # [1, 12, 6, 7, 8]
print(list(res))
