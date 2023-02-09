"""
10.Напишите функцию Python, которая принимает список и возвращает новый список с 
уникальными элементами первого списка. Примечание: не используйте набор коллекций
"""
def unique(lst):
    x = []
    for elem in lst:
        if not elem in x:
            x.append(elem)
    return x

list = [1, 2, 1, 2, 4, 3, 3, 3, 3, 3]
print(unique(list))