import os
path = input("Путь: ")
if os.path.exists(path):
    print("Файл найден")
    if os.access(path, os.W_OK):
        os.remove(path)
        print("Файл успешно удален")
    else:
        print("У вас нет разрешение")
else:
    print("Файл не найден")