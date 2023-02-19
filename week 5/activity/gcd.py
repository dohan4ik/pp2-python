a = int(input())
b = int(input())
if a > b:
    i = 1
    while i <= b:
        if b % i == 0 and a % i == 0:
            gcd = i 
        i += 1
elif a == b:
    gcd = a
else:
    i = 1
    while i <= a:
        if b % i == 0 and a % i == 0:
            gcd = i
        i += 1
print(gcd)