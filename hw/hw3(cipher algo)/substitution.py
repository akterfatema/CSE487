def substitution_encrypt(plaintext, codebook):
    ciphertext = ''

    for char in plaintext:
        if char.isalpha():
            encrypted_char = codebook.get(char.upper(), char)
            ciphertext += encrypted_char
        else:
            ciphertext += char

    return ciphertext


def substitution_decrypt(ciphertext, codebook):
    plaintext = ''

    for char in ciphertext:
        if char.isalpha():
            decrypted_char = ''
            for key, value in codebook.items():
                if value == char.upper():
                    decrypted_char = key
                    break
            plaintext += decrypted_char
        else:
            plaintext += char

    return plaintext


plaintext = "HELLO WORLD"
codebook = {
    'A': 'Q',
    'B': 'W',
    'C': 'E',
    'D': 'R',
    'E': 'T',
    'F': 'Y',
    'G': 'U',
    'H': 'I',
    'I': 'O',
    'J': 'P',
    'K': 'A',
    'L': 'S',
    'M': 'D',
    'N': 'F',
    'O': 'G',
    'P': 'H',
    'Q': 'J',
    'R': 'K',
    'S': 'L',
    'T': 'Z',
    'U': 'X',
    'V': 'C',
    'W': 'V',
    'X': 'B',
    'Y': 'N',
    'Z': 'M',
}
ciphertext = substitution_encrypt(plaintext, codebook)
print("Ciphertext:", ciphertext)
ciphertext = "ITSSG VGKSR"
plaintext = substitution_decrypt(ciphertext, codebook)
print("Plaintext:", plaintext)
