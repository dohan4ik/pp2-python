"""
 Напишите определение класса Point. Объекты этого класса должны иметь

        метод show для отображения координат точки
        метод move для изменения этих координат
        метод dist, который вычисляет расстояние между двумя точками
"""

import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, x, y):
        self.x += x
        self.y += y
        print(f"Измененые кординты: {self.x}, {self.y}")
    def dist(self, start_point):
        x = self.x - start_point
        y = self.y - start_point
        print(math.sqrt(x ** 2 + y ** 2))
res = Point(int(input()), int(input()))
res.dist(0) 