from functools import reduce
numbers = [5, 6, 7]
print(reduce(lambda x, y: x * y, numbers))