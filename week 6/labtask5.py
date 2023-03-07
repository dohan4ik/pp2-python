import re
a = input()
result = re.findall(r'a\S+b', a)
print(result)