class Shape:
     def __init__(self):
         pass
     def area(self):
        return 0
class Square(Shape):
     length = None
     def __init__(self, length):
         self.get_inf(length)
         self.area()
     def get_inf(self, length):
         self.length = length
     def area(self):
         print(self.length ** 2)

a = Square(int(input()))