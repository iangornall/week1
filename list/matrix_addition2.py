matrix1 = [ [5, 3, 53, 45], [3, 534, 35, 345], [3, 534, 35, 345] ]
matrix2 = [ [3434, 5, 32, 324], [352, 35, 324, 346], [3, 534, 35, 345] ]
total = []
for i, row in enumerate(matrix1):
    total.append([])
    for j, number1 in enumerate(matrix2):
        total[i].append(number1 + matrix2[i][j])
print total