encoded = raw_input("Encoded string: ")
decoded = ""
for char in encoded:
    ascii_code = ord(char)
    if (ascii_code > 64 and ascii_code < 78) or (ascii_code > 96 and ascii_code < 110):
        decoded += chr(ascii_code + 13)
    elif (ascii_code > 77 and ascii_code < 91) or (ascii_code > 109 and ascii_code < 123):
        decoded += chr(ascii_code - 13)
    else:
        decoded += char
print decoded