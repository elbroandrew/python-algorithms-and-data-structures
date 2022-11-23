"""
'abcabcabc', 2 => 'abcabc'
'aabbcc', 1 => 'abc'
"""

string = "aabbcc"


def clean_string(txt, repeats):
    d = {}
    for ch in txt:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1

    return ''.join([*filter(lambda x: d[x] >= repeats, d)]) * repeats


g = clean_string(string, 1)
print(g)