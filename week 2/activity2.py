x = input()
z = ""
#121
for i in range(len(x)):
    z += x[len(x) - (i + 1)]
if z == x:
    print(True)
else:
    print(False)
