with open("filetask4lab6.txt", "r") as filetask4lab6:
    readed = filetask4lab6.read()
with open("filetask7lab6.txt", "w") as filetask7lab6:
    filetask7lab6.write(readed)
print("файд скопирован")