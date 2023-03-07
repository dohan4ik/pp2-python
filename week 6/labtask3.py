import re
a = input()
result =  re.findall(r'[a-z]+-[a-z]+', a)
print(result) 