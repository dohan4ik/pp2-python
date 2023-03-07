import re
a = input()
if re.search(r'^a(b){3}$', a):
    print(True)
elif re.search(r'a(b){2}', a):
    print(True)
else:
    print(False)