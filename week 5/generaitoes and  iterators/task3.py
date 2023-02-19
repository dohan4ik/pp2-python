# Определите функцию с генератором, которая может перебирать числа, кратные 3 и 4, в заданном диапазоне от 0 до n.
def divisible(a):
    for i in a:
        if i % 3 == 0 and i % 4 == 0:
            print(i)
n = int(input())
a =(i for i in range(1, n))
divisible(a)