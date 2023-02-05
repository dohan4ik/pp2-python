class Shape:
    def __init__(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.ded(length, width)
        self.area()
    def ded(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        print(self.length * self.width)
a = Rectangle(int(input()), int(input()))