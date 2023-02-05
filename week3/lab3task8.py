"""
"""
def my_function(nums):
    x = [0, 0, 7, 'a']
    for num in nums:
        if num == x[0]:
            x.pop(0)
    return x==['a']

print(my_function([1,2,4,0,0,7,5]))
print(my_function([1,0,2,4,0,5,7]))
print(my_function([1,7,2,0,4,5,0]))