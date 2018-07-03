def init():
    nums = [34, 35, 436, -436, -34]
    factor = 5
    print multiply(nums, factor)

def multiply(nums, factor):
    products = []
    for num in nums:
        products.append(num * factor)
    return products

init()