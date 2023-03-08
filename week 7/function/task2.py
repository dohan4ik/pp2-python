def count(a):
    upper_cnt = 0
    lower_cnt = 0
    for i in a:
        if i.isupper():
            upper_cnt += 1
        elif i.islower():
            lower_cnt += 1
    print("Number of upper case letters:", upper_cnt)
    print("Number of lower case letters:", lower_cnt)
a = input("Введите строку: ")
count(a)
