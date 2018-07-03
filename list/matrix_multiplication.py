def init():
    matrix1 = [ [5, 3, 2], [4, 8, 1] ]
    matrix2 = [ [1], [8], [4] ]
    print multiply(matrix1, matrix2)

def multiply(matrix1, matrix2):
    product = []
    for row in range(len(matrix1)):
        product.append([])
        for col in range(len(matrix2[0])):
            product[row].append(0)
            for k in range(len(matrix1[0])):
                product[row][col] += matrix1[row][k] * matrix2[k][col]
    return product

init()