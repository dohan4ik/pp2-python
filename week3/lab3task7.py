"""
7.Учитывая список ints, верните True, если массив содержит 3 рядом с 3.
"""
def my_function(x):
    for i in range(len(x) - 1):
        if x[i] == 3 and x[i + 1] == 3:
            return True
    return False

print(my_function([1, 3, 3]))
print(my_function([1, 3, 1, 3]))
print(my_function([3, 1, 3]))