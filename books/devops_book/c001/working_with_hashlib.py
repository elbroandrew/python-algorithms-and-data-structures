import hashlib

secret = "This is the secret password"
bsecret = secret.encode()  # convert to binary string

m = hashlib.md5()
m.update(bsecret)

print(m.digest())