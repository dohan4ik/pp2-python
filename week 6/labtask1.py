import re
a = str(input())
if re.search(r'^a(b)*$', a):
    print(True)
elif re.search(r'^a(0)', a):
    print(True)
else:
    print(False)