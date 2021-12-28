def color_picker(text: str, color: str):
    colors = ("yellow", "green", "cyan")
    if type(text) is not str:
        raise TypeError("Text param should be string")
    if color not in colors:
        raise ValueError("color is not valid")
    print(f"{text} {color}")

# color_picker("bar", "foo")


'''try except'''
try:
    foo
except:
    print("NO FOO")
print("after try")


'''example 2'''
d = dict(a=1, b=2)
def return_key(d: dict, key: str):
    try:
        return d[key]
    except KeyError:
        return None
return_key(d, 'c') # None


'''try, except, finally'''
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print('DO NOT DIVIDE BY ZERO.')
    except TypeError as err:
        print('a and b must floats or ints')
        print(err)
    else:
        print(f"{a} divided by {b} is {result}")
divide(1, 'v')

