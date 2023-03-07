import re 
a = input()
#result = re.split(r'[A-Z]', a)
result = re.findall(r'[A-Z][a-z]*', a)
print(result)