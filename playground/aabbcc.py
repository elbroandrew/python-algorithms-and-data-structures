"""
'abcabcabc', 2 => 'abcabc'
'aabbcc', 1 => 'abc'
"""

string = "aabbcc"


def clean_string(txt, repeats):
    res_str = ""
    for ch in txt:
        if txt.count(ch) >= repeats:
            res_str += ch

    return res_str


g = clean_string(string, 1)
print(g)
