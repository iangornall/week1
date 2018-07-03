string = raw_input("Word: ")
newstr = ""
vowels = ['a', 'e', 'i', 'o', 'u']
stop = False
for i in range(len(string)):
    char = string[i]
    if char.lower() in vowels and i != len(string) - 1 and string[i+1] == char and stop == False:
        newstr += char * 5
        stop = True
    else: 
        if char not in vowels:
            stop = False
        if stop == False:
            newstr += char
print newstr 
