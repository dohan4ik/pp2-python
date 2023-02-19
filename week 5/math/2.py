"""
Write a Python program to calculate the area of a trapezoid.(трапеция ауданы)
Height: 5
Base, first value: 5
Base, second value: 6
Expected Output: 27.5
"""
import math
h = int(input("Height: "))
a = int(input("Base, first value: "))
b = int(input("Base, second value: "))
s = ((a + b) / 2) * h
print(f"Area of a trapezoid: {s}")