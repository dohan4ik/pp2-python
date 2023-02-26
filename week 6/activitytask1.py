import re
a = str(input())
x = re.sub("Python", "Java", a, count=0, flags=0)
print(x)
