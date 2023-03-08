import os
path = input("Path:")
directories = []
files = []
dir_and_fil = []
for i in os.listdir(path):
    if os.path.isdir(os.path.join(path, i)):
        directories.append(i)
        dir_and_fil.append(i)
    elif os.path.isfile(os.path.join(path, i)):
        files.append(i)
        dir_and_fil.append(i)        
print("Directories:", directories)
print("Files:", files)
print("Directory and Files:", dir_and_fil)