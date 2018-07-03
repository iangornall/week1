def init():
    nums = [34, 35, 436, 436, 34]
    print filter_even(nums)

def filter_even(nums):
    evens = []
    for num in nums:
        if num % 2 == 0:
            evens.append(num)
    return evens

init()