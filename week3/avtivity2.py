x = input()
y = str(x)
z = ""
if y[0] == '-':
    z += '-'
    i = 0  
    while i < len(y) - 1:
        z += y[len(y) - (i + 1)]
        i += 1
else:
    i = 0
    while i < len(y):
        z += y[len(y) - (i + 1)]
        i += 1
q = ""
for i in range(len(z)):
    if i == 0:
        if z[i] == '0':
            continue
        else:
            q += z[i]
    else:
        q += z[i]
print(q)