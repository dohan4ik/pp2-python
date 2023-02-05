"""
5.Напишите функцию, которая принимает строку от пользователя и выводит все перестановки этой строки.
"""
def is_permutations(data, index=0):
    if index == len(data) - 1:
        print(''.join(data))
    else:
        for i in range(index, len(data)):
            data[index], data[i] = data[i], data[index]
            is_permutations(data, index + 1)
            data[index], data[i] = data[i], data[index]

x = input()
is_permutations(list(x))