from typing import List

"""
for [
    'a', 'b', 'c',
    'a', 'b',
    'a'
] == 'a' should return True
"""

def most_frequent_string(list_of_strings: List):
    if not len(list_of_strings) == 0:
        dict_of_strings = {k: list_of_strings.count(k) for k in list_of_strings}
        return max(dict_of_strings, key=dict_of_strings.get)
    else:
        raise ValueError('list should not be empty')


ll = ['a', 'b', 'c', 'a', 'c', 'c']
ll2 = [
    'a', 'b', 'c',
    'a', 'b',
    'a'
]
ll3 = []

print( most_frequent_string(ll3) == 'a')
