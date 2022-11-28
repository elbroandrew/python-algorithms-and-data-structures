import hashlib

user = "a"
user_hash = hashlib.sha256(user.encode()).hexdigest()
print(user.encode())
print(user_hash)

