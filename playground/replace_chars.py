import string

# алфавит сдвинут, нужно заменить буквы и получить текст.

# naive solution

s = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

# mm = string.ascii_lowercase[2::] + string.ascii_lowercase[:2]
# zipped = dict(zip(string.ascii_lowercase, mm))

# #print(zipped)


# def decipher(text: str, m: dict):

#   res = ""
#   for c in text:
#     if c in m:
#       res += m[c]
#     else:
#       res += c

#   print(res)


# decipher(s, zipped)


# solution with 'maketrans'

intab = string.ascii_lowercase
outtab = string.ascii_lowercase[2::] + string.ascii_lowercase[:2]
transtab = str.maketrans(intab, outtab)
print(transtab)

s = s.translate(transtab)
print(s)