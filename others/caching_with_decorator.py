import time
# caching

def cache_func(f):
  cache = {}
  def wrapper(a):
    if a in cache:
      return cache[a]

    cache[a] = f(a)
    return cache[a]
  return wrapper


@cache_func
def func(num1):
  return num1**10

t1 = time.time()
print(func(4))
t2 = time.time()
print(t2 - t1)

t3 = time.time()
print(func(4))
t4 = time.time()
print(t4 - t3)

