hex = [i for i in range(0, 10)]

for i in "ABCDEF":
    hex.append(i)

x = 3331
base = 16
res = []

while x > base:
    y = x // base
    res.insert(0, str(hex[x - y* base]))
    x = y
    

if x in range(0, base):
    res.insert(0, str(hex[x]))

res = ''.join(res)

print(res)