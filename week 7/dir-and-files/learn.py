import os
#изменение файла
os.rename("имя файла", "изменение имени файла")
#удаление файла
os.remove("имя фала которое нужно удалить")
#создать файл
os.mkdir("namefile")
#создать папку в определенном месте
os.chdir("C:/Users/DARkHAN/Desktop/python/week 7") #котолок
os.mkdir("testfile")
#чтобы узнать котолок 
print(os.getcwd())
#если хотим удалить файлы в определенном
os.chdir("C:/Users/DARkHAN/Desktop/python/week 7")
os.rmdir("test")
