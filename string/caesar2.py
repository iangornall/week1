encoded = raw_input("Encoded string: ")
decoded = ""
lowercase = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
uppercase = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for char in encoded:
    if char in lowercase:
        for i in range(len(lowercase)):
            if lowercase[i] == char:
                index = i
        if index < 13:
            decoded += lowercase[index + 13]
        elif index >= 13:
            decoded += lowercase[index - 13]
    elif char in uppercase:
        for i in range(len(uppercase)):
            if uppercase[i] == char:
                index = i
        if index < 13:
            decoded += uppercase[index + 13]
        elif index >= 13:
            decoded += uppercase[index - 13]
    else:
        decoded += char
print decoded