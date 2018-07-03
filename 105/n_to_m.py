start = int(raw_input('Start from: '))
end = int(raw_input('End on: '))
if end >= start:
    for n in range(start, end + 1):
        print n