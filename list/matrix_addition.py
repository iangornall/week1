
def init():
    matrix1 = [ [5, 3, 53, 45], [3, 534, 35, 345], [3, 534, 35, 345] ]
    matrix2 = [ [3434, 5, 32, 324], [352, 35, 324, 346], [3, 534, 35, 345] ]
    print add(matrix1, matrix2)

def add(matrix1, matrix2):
    total = []
    num_rows = len(matrix1)
    num_cols = len(matrix1[0])
    for i in range(num_rows):
        total.append([])
        for j in range(num_cols):
            total[i].append(matrix1[i][j] + matrix2[i][j])
    return total

init()