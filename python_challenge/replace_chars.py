import string

s = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""


mm = string.ascii_lowercase[2::] + string.ascii_lowercase[:2]
zipped = dict(zip(string.ascii_lowercase, mm))

#print(zipped)


def decipher(text: str, m: dict):

  res = ""
  for c in text:
    if c in m:
      res += m[c]
    else:
      res += c

  print(res)


decipher(s, zipped)