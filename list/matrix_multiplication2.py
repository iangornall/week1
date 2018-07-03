matrix1 = [ [5, 3, 2], [4, 8, 1] ]
matrix2 = [ [1, 4], [8, 3], [4, 4] ]
product = []
for row in range(len(matrix1)):
    product.append([])
    for col in range(len(matrix2[0])):
        product[row].append(0)
        for i in range(len(matrix1[0])):
            product[row][col] += matrix1[row][i] * matrix2[i][col]
print product