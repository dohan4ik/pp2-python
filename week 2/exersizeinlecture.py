"""
import random
a = random.randint(1, 100)
print(a)
i = 00
while i < 8:
    myNum = int(input("Insert num:"))
    if a == myNum:
        print("Win attempt:", (i + 1))
        break
    elif a > myNum: 
        print("Youur number less than computor")
    else: 
        print("Your number greater than compuuter")
        i = i + 1
"""  

