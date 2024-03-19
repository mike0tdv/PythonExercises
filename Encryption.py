import random
import string

chars = string.punctuation + string.digits + string.ascii_letters + " "
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"Chars: {chars}")
# print(f"Key: {key}")

# Encryption
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Encrypted message: {cipher_text}")

# Decryption
ans = input("Do you want to get the decrypted message(y/n): ").lower()
if ans == "y":
    plain_text1 = ""
    for letter in cipher_text:
        index = key.index(letter)
        plain_text1 += chars[index]
    print(f"The decrypted message: {plain_text1}")


elif ans == "n":
    print("Ok! Bye!")
else: print("Not a valid answer! Bye!")