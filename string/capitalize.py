string = raw_input('Sentence: ')
newstr = ''
punctuation = ".!?"
lowercase = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
uppercase = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

if string[0] in lowercase:
    for i in range(len(lowercase)):
        if string[0] == lowercase[i]:
            newstr += uppercase[i]
else:
    newstr += string[0]

capitalize = False
for i in range(1, len(string)):
    char = string[i]
    if char in punctuation:
        capitalize = True
    if capitalize == True and char in lowercase:
        for j in range(len(lowercase)):
            if string[i] == lowercase[j]:
                char = uppercase[j]
        capitalize = False
    if capitalize == True and char in uppercase:
        capitalize = False
    newstr += char

print newstr