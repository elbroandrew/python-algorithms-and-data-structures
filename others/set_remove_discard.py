d = {1, 2, 3, 4, 5}

# различие только в эксепшене, один выкидывает, второй - нет.

d.remove(6) # exception
print(d)

d.discard(6) # ничего