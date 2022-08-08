s = "123457"  # 25000 should be 52
l = len(s)

if l == 5:
	x = int(s[::-1])
	print(x)

elif l == 6:
	c = s[-5::]
	start = s[0]
	result = int(start + s[:-6:-1])

	print(result)