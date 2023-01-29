x = input()
list1 = []
list2 = []
for i in x:
    cnt = 0
    if i in list1:
        continue
    else:
        for j in x:
            if i == j:
                cnt += 1
        list1.append(i)
        list2.append(cnt)
for i in range(len(list1)):
    print(list1[i], list2[i], sep = "->")
