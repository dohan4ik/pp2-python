"""
. Определите класс Shape и его подкласс Square. Класс Square имеет функцию init, которая принимает в качестве аргумента длину. Оба класса 
имеют функцию area, которая может вывести площадь фигуры, где площадь Shape по умолчанию равна 0.
"""
class Shape:
     def area(self):
        return 0
class Square(Shape):
     length = None
     def __init__(self, length):
         self.length = length
         self.area()
     def area(self):
         print(self.length ** 2)

a = Square(int(input()))