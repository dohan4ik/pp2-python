"""Напишите программу на Python для проверки существования 
или отсутствия заданного пути. 
Если путь существует, найдите имя файла и часть каталога по заданному пути."""
import os
path = input("Path: ")
if os.path.exists(path):
    print("Путь существует")
    print("Путь к файлу: ", os.path.dirname(path))
    print("Имф файла: ", os.path.basename(path))
else:
    print("Путь не существует")
                                          #C:\Users\DARkHAN\Desktop\python