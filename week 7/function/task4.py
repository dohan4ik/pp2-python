import math
import time
def sqrt(num):
    return float(math.sqrt(num))
ms = (int(input("Введите время замедления в милисекундах: ")))
s = ms / 1000
n = int(input("Введите число: "))
res = float(sqrt(ms))
print(f"Square root of {ms} after {n} is:", int(res))