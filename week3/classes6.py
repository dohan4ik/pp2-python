"""
6. Напишите программу, которая может фильтровать простые числа 
в списке с помощью функции filter. Примечание: Используйте лямбду для определения анонимных функций.
"""

a = int(input()) 
nums = []
primes = []
cnt = 0
for i in range(a):
    nums.append(int(input()))
for i in nums:
    if i != 1:
       for j in range(2, i):
           if i % j == 0:
              cnt += 1
           else:
              continue
       if cnt == 0:
          primes.append(i)
       cnt = 0
    else:
        continue
print(primes)