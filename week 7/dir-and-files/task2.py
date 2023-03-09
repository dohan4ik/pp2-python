import os
path = input("Путь:")
if os.path.exists(path):
    print("Этот путь существует:", path)
else:
    print("Этот путь не существует", path)
if os.access(path, os.R_OK):
    print("Есть разрешение на чтени.")
else:
    print("Нет разрешение на чтение")
if os.access(path, os.W_OK):
    print("Есть разрешение на запись")
else:
    print("Нет разрешение на запись")
if os.access(path, os.X_OK):
    print("Есть разрешение на выполнение")
else:  
    print("Нет разрешениена на разрешение")            #C:\Users\DARkHAN\Desktop\python