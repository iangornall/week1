string = 'okay sure'
print string[::-1]


for i in range(len(string)):
    newstr += string[len(string) - i - 1]
print newstr