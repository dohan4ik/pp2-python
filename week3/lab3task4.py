"""
4.Вам дан список чисел, разделенных пробелами. Напишите функцию filter_prime, которая будет принимать список 
чисел в качестве аргумента и возвращать только простые числа из списка.
"""
def filter_primes(numbers):
    primetest = lambda num: num > 1 and all(num % i != 0 for i in range(2, num, 1))

    return list(filter(primetest, numbers))
x = input()
numbers = list(map(int, x.split()))
print(filter_primes(numbers))