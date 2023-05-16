import hashlib
new_hasher = hashlib.sha1()
new_hasher.update(b'This is the secret message')
print(new_hasher.hexdigest())

import hashlib
hasher = hashlib.md5()
hasher.update(b'This is the secret message')
hash_hex = hasher.hexdigest()
print(hash_hex)

# import hashlib

# message = "Hello, world!"
# sha = hashlib.sha256()
# sha.update(message.encode())
# digest = sha.digest()
# print("Original message:", message)
# print("SHA-256 digest:", digest.hex())
# sha = hashlib.sha256()
# received_message = "Hello, world!"
# sha.update(received_message.encode())
# received_digest = sha.digest()

# if digest == received_digest:
#     print("Message integrity check passed.")
# else:
#     print("Message integrity check failed.")
