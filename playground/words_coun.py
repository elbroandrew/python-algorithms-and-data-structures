from collections import Counter

'''
"AAAABBBCCD" -> 4A3B2C1D
'''

data = "AAAABBBCCD"

c = Counter(data)

r = [f"{v}{k}" for k,v in c.most_common()]
res = "".join(r)  
print(res)