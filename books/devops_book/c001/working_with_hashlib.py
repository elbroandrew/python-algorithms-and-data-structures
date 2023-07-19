import hashlib
from cryptography.fernet import Fernet

secret = "This is the secret password"
bsecret = secret.encode()  # convert to binary string

m = hashlib.md5()
m.update(bsecret)

print(m.digest())

# example with cryptography Fernet (AES algo)
key = Fernet.generate_key()
print(key)
# encrypt the data using Fernet object (to store the key)
f = Fernet(key)
message = b'Hello World'
encrypted = f.encrypt(message)
print(encrypted)
# decrypt
print(f.decrypt(encrypted))

