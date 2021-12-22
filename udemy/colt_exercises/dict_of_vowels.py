# {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
s = 'aeiou'

answer = {char: 0 for char in s}
print(answer)

# 2 solution
answer2 = dict.fromkeys(s, 0)
print(answer2)
