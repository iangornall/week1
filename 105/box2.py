width = int(raw_input('Width? '))
height = int(raw_input('Height? '))
solid_line = ''
for i in range(width):
    solid_line += '*'
print solid_line
for n in range(height - 2):
    print '*' + (' ' * (width - 2)) + '*'
print solid_line