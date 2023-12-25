def vigenere_encrypt(plaintext, keyword):
    plaintext = plaintext.upper()
    keyword = keyword.upper()
    ciphertext = ''
    keyword_index = 0

    for char in plaintext:
        if char.isalpha():
            shift = ord(keyword[keyword_index]) - ord('A')
            encrypted_char = chr(
                (ord(char) - ord('A') + shift) % 26 + ord('A'))
            ciphertext += encrypted_char
            keyword_index = (keyword_index + 1) % len(keyword)
        else:
            ciphertext += char

    return ciphertext


def vigenere_decrypt(ciphertext, keyword):
    plaintext = ''
    keyword = keyword.upper()
    keyword_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(keyword[keyword_index]) - ord('A')
            decrypted_char = chr(
                (ord(char) - ord('A') - shift) % 26 + ord('A'))
            plaintext += decrypted_char
            keyword_index = (keyword_index + 1) % len(keyword)
        else:
            plaintext += char

    return plaintext



plaintext = "HELLO"
keyword = "KEY"
ciphertext = vigenere_encrypt(plaintext, keyword)
print("Ciphertext:", ciphertext)
plaintext = vigenere_decrypt(ciphertext, keyword)
print("Plaintext:", plaintext)
