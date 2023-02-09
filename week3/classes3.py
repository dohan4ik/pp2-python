"""
. Определите класс с именем Rectangle, который наследуется от класса Shape из задания 2.
 Экземпляр класса может быть построен по длине и ширине. Класс Rectangle имеет метод, который может вычислять площадь.

"""
class Shape:
    def __init__(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area()
    def area(self):
        print(self.length * self.width)
a = Rectangle(int(input()), int(input()))