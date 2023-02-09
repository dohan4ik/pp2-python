"""
8. Напишите функцию, которая принимает список целых чисел и возвращает True, если он содержит 007 по порядку
def spy_game(nums):
    pass

    spy_game([1,2,4,0,0,7,5]) --> True
    spy_game([1,0,2,4,0,5,7]) --> True
    spy_game([1,7,2,0,4,5,0]) --> False
"""
def my_function(nums):
    x = [0, 0, 7, 'a']
    for num in nums:
        if num == x[0]:
            x.pop(0)
    return x == ['a']

print(my_function([1,2,4,0,0,7,5]))
print(my_function([1,0,2,4,0,5,7]))
print(my_function([1,7,2,0,4,5,0]))