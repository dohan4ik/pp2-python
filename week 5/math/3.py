"""
Write a Python program to calculate the area of regular polygon.
Input number of sides: 4
Input the length of a side: 25
The area of the polygon is: 625
"""
import math
s = int(input("Number of sides: "))
l = int(input("Length: "))
g = math.cos(180 / s)
p = l * s
r = (l / (2 * math.tan(math.pi / s)))
a = (r * p) / 2
print(int(a))
