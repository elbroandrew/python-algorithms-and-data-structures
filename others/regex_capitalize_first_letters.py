import re

s = "peter piper picked a peck of pickled peppers."


result = re.sub(r'(\b(\w))', lambda x: x.group()[0].upper(), s)
print(result)
