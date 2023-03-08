with open("filetask4lab6.txt", "r") as file:
    cnt = 0
    for line in file:
        cnt += 1
print("Количество строк", "filetask4lab6.txt", ":", cnt)
