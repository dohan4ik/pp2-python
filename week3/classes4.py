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
        print(f"Это новые данные: {self.x}, {self.y}")
    def dist(self, start_point):
        x_new = self.x - start_point
        y_new = self.y - start_point
        print(math.sqrt(x_new ** 2 + y_new ** 2))
res = Point(int(input()), int(input()))
res.dist(0) 