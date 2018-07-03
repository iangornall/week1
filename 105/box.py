width = int(raw_input('Width? '))
height = int(raw_input('Height? '))
print '*' * width
for n in range(height - 2):
    print '*' + (' ' * (width - 2)) + '*'
print '*' * width