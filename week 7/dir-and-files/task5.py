"""Напишите программу на языке Python для записи списка в файл."""
list = ["artur", "darkhan", "marat", "alisher"] 
with open("file5task6lab.txt", "w") as file:
    for i in list:
        file.write(i + "\n")
    #C:\Users\DARkHAN\Desktop\python