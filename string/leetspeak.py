letters = ['A', 'E', 'G', 'I', 'O', 'S', 'T']
numbers = [4, 3, 6, 1, 0, 5, 7]
phrase = 'okay fine'
l33t = ''
for char in phrase:
    if char.upper() in letters:
        l33t += str(numbers[letters.index(char.upper())])
    else:
        l33t += char
print l33t