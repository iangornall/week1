height = int(raw_input('Height: '))
for n in range(height):
    print (' ' * (height - n)) + '*' * (1 + n * 2)

    