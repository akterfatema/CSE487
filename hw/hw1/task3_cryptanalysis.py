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
            result += chr((ord(char) - s - 65) % 26 + 65)
        # encypt_func lowercase characters in plain txt
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)
    print('Sentence is : ',result) 

def calculate_frequency(string):
    frequency = {}

    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    max_key = max(frequency, key=frequency.get)
    #print(max_key)
    letter_most_frequent = ['e', 't', 'n', 's', 'a', 'o', 'i' ]
    for i in letter_most_frequent:
        print('for letter :',i)
        decypt_func(string, abs(ord(max_key)-ord(i)))
    return frequency


# Example usage
string = "fatemaakter"
s=3
encypt_func(string, s)
frequency = calculate_frequency(string)

# Print the frequencies
# for char, count in frequency.items():
#     print(char + ": " + str(count))
