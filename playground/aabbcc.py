"""
'abcabcabc', 2 => 'abcabc'
'aabbcc', 1 => 'abc'
"""

string = "abcabcabc"


def clean_string(txt, repeats):
    res_str = ""
    chars = dict.fromkeys(set(txt), 0)
    for ch in txt:
        chars[ch] += 1
        if chars[ch] <= repeats:
            res_str += ch

    return res_str


g = clean_string(string, 2)
print(g)
