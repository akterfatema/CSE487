def encypt_func(txt, s):
    result = ""


# transverse the plain txt
    for i in range(len(txt)):
        char = txt[i]
        # encypt_func uppercase characters in plain txt

        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        # encypt_func lowercase characters in plain txt
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result


def decypt_func(txt, s):
    result = ""


# transverse the plain txt
    for i in range(len(txt)):
        char = txt[i]
        # encypt_func uppercase characters in plain txt

        if (char.isupper()):
            result += chr((ord(char) -s - 65) % 26 + 65)
        # encypt_func lowercase characters in plain txt
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)
    return result


# check the above function
txt = "Bangladesh"
s = 3

print("Plain txt : " + txt)
print("Shift pattern : " + str(s))
print("Cipher: " + encypt_func(txt, s))
text = encypt_func(txt, s)
print("Decrypt text: " + decypt_func(text, s))
