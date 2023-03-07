import re
a = input()
result_o1 = re.sub(r' ', ',', a)
result_t2 = re.sub(r'\.', ':', a)
print(result_o1)
print(result_t2)