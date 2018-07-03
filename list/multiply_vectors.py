def init():
    vector1 = [34, 35, 436, -436, -34]
    vector2 = [3, 5, 4, 3, 435]
    print multiply(vector1, vector2)

def multiply(vector1, vector2):
    products = []
    for i in range(len(vector1)):
        products.append(vector1[i] * vector2[i])
    return products

init()