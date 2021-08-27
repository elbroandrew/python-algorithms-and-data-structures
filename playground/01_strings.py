"""
slicing
[start:stop:step]
"""
my_string = "hello"
print(my_string[1:4])

"""
[::2] from start to end and step 2
also reverse string:
[::-1]
"""
print(my_string[::-1])

""" strings are IMMUTABLE
my_string[0] = 'z' //type error
"""
