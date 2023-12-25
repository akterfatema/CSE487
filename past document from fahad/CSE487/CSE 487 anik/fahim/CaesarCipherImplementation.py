#encrypt cypher text
def cipher_encrypt(plain_text, shift):
    encrypted = ""
    for c in plain_text:
        if c.isupper():
            c_index = ord(c) - ord('A')
            c_shifted = (c_index + shift) % 26 + ord('A')
            encrypted += chr(c_shifted)

        elif c.islower():
            c_index = ord(c) - ord('a')
            c_shifted = (c_index + shift) % 26 + ord('a')
            encrypted += chr(c_shifted)

        elif c.isdigit():
            encrypted += str((int(c) + shift) % 10)

        else:
            encrypted += c

    return encrypted


#Brute force to decrypt cypher text
def cipher_decrypt_lower(ciphertext, key):
    decrypted = ""
    for c in ciphertext:
        if c.islower():
            c_index = ord(c) - ord('a')
            c_og_pos = (c_index - key) % 26 + ord('a')
            c_og = chr(c_og_pos)
            decrypted += c_og
        elif c.isupper():
            c_index = ord(c) - ord('A')
            c_og_pos = (c_index - key) % 26 + ord('A')
            c_og = chr(c_og_pos)
            decrypted += c_og
        elif c.isdigit():
            decrypted += str((int(c) - key) % 10)
        else:
            decrypted += c
    return decrypted


plain_text = "i love this thing."
ciphertext = cipher_encrypt(plain_text, 7)
print("Plain text message:\n", plain_text)
print("Encrypted ciphertext:\n", ciphertext)

for i in range(0, 26):
    plain_text = cipher_decrypt_lower(ciphertext, i)
    print("For key {}, decrypted text: {}".format(i, plain_text))

#breaking a substitution cipher using letter frequency
print("Cipher Text: ", ciphertext)
stored_letters = {}

for char in ciphertext:
    if char not in stored_letters:
        stored_letters[char] = 1
    else:
        stored_letters[char] += 1

print(stored_letters)
attempt = ciphertext.replace("p", "I")
attempt = attempt.replace("a", "T")
attempt = attempt.replace("o", "H")
attempt = attempt.replace("s", "L")
attempt = attempt.replace("u", "N")
attempt = attempt.replace("z", "S")
attempt = attempt.replace("n", "G")
attempt = attempt.replace("v", "O")
attempt = attempt.replace("c", "V")
attempt = attempt.replace("l", "E")

print("Plain Text: ", attempt)
