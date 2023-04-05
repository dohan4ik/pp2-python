import re
a = input()
result_o1 = re.sub(r' ', ':', a)
result_o1 = re.sub(r'\.', ':', result_o1)
result_o1 = re.sub(r',', ':', result_o1)
print(result_o1)