hex = [i for i in range(0, 10)]

for i in "ABCDEF":
    hex.append(i)

x = 3331
base = 16
t = x
y = x
res = ""

while t > base:
    t = t // base
    o = y - t * base
    y = t
    res += str(hex[o])

if y in range(0, base):
    res += str(hex[y])

res = res[::-1]

print(res)