import string
letters = list(string.ascii_uppercase)
for i in letters:
    filename = i + ".txt"
    with open(filename, "w") as file:
        file.write("This is file " + filename)
        #C:\Users\DARkHAN\Desktop\python