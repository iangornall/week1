def init():
    l33t_dict = {'A': '4', 'E': '3', 'G': '6', 'I': '1', 'O': '0', 'S': '5', 'T': '7'}
    phrase = 'okay fine'
    print convert(phrase, l33t_dict)

def convert(phrase, dictionary):
    converted = ''
    for char in phrase:
        if char.upper() in dictionary:
            char = dictionary[char.upper()]
        converted += char
    return converted

init()