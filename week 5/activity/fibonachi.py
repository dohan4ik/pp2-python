x = int(input())
i = 0
l = []
while(i < x):
    if i == 0:
        l.append(0)
        num1 = i
    elif i == 1:
        l.append(1)
        num2 = i
    else:
        num_next = num1 + num2
        l.append(num_next)
        num1 = num2
        num2 = num_next
    i += 1
print(l)