def count_up_to_max(max):
    count = 1
    while count <= max:
        yield count
        count += 1

# counter = count_up_to_max(5)
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))


# GENERATOR EXPRESSION
g = (num for num in range(1, 10))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
