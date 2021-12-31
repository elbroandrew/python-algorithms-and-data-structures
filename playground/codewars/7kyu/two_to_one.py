"""
Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
"""

def longest(a: str, b: str) -> str:
    my_set = set(a)
    for letter in b:
        my_set.add(letter)
    return ''.join(sorted(my_set))

longest("aretheyhere", "yestheyarehere")

def longest2(a, b):
    return ''.join((sorted({i for i in a + b})))

print(longest2("aretheyhere", "yestheyarehere"))