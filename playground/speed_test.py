from time import time

n = 10000000

value, start = 0, time()
for i in range(n):
    value = (value + 1) % 2
print(f"% 2 time: {time() - start}")

value, start = 0, time()
for i in range(n):
    value = value ^ 1
print(f"XOR time: {time() - start}")

value, start = 0, time()
for i in range(n):
    value = not value
print(f"not time: {time() - start}")
