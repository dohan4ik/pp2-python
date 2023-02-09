"""
6. Напишите программу, которая может фильтровать простые числа 
в списке с помощью функции filter. Примечание: Используйте лямбду для определения анонимных функций.
"""

a = int(input()) 
nums = []
for i in range(a):
    nums.append(int(input()))
def filter(nums):
   primes = []
   for i in nums:
    cnt = 0   
    if i == 1:
       continue
    else:
       for j in range(2, i):
           if i % j == 0:
              cnt += 1
           else:
              continue
       if cnt == 0:
          primes.append(i)
       cnt = 0
       return primes
print(filter(nums))