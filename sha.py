# https://colab.research.google.com/drive/1NG1Uw6UWe-K0RbDC7yl1QzuYWBNbjT0W#scrollTo=Dfdc24Nc5jWd
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

# abhijet
# import hashlib

# def calculate_sha256(message):
#     sha256 = hashlib.sha256(message.encode('utf-8')).hexdigest()
#     return sha256

# def check_integrity(message, original_hash):
#     calculated_hash = calculate_sha256(message)
#     if calculated_hash == original_hash:
#         print("Integrity Check: Passed")
#     else:
#         print("Integrity Check: Failed")

# # Example usage
# original_message = "Hello, World!"
# original_hash = calculate_sha256(original_message)

# print("Original Message:", original_message)
# print("Original Hash:", original_hash)

# # Tampering the message
# tampered_message = "Hello, World! (tampered)"

# print("\nTampered Message:", tampered_message)
# check_integrity(tampered_message, original_hash)