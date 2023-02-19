"""
Реализуйте генератор квадратов для получения квадрата всех чисел от (a) до (b). 
Протестируйте его с помощью цикла "for" и выведите каждое из полученных значений.
"""
import math
a = int(input())
b = int(input())
x = int(math.sqrt(a))
y = int(math.sqrt(b))
g = (i**2 for i in range(x, y + 1))
for i in g:
    print(i)
