def unique(lst):
    x = []
    for elem in lst:
        if not elem in x:
            x.append(elem)
    return x

list = input()
print(unique(list))