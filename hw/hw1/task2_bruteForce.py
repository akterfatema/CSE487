

def decypt_func(txt):
   
    j =0

# transverse the plain txt
    while(j < 26):
        result = ""
        for i in range(len(txt)):
         char = txt[i]
        # encypt_func uppercase characters in plain txt

         if (char.isupper()):
            result += chr((ord(char) - j - 65) % 26 + 65)
        # encypt_func lowercase characters in plain txt
         else:
            result += chr((ord(char) - j - 97) % 26 + 97)
        print(result)
        j +=1


    


txt = "Edqjodghvk"
decypt_func(txt)

