import os
path = input("Путь: ")
if os.path.exists(path):
    print("Файл найден")
    if os.access(path, os.R_OK):
        os.remove(path)
        print("Файл успешно удален")
    else:
        print("У вас нет разрешение")
else:
    print("Файл не найден")              #C:\Users\DARkHAN\Desktop\python\remove