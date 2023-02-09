"""
1. Определите класс, который имеет как минимум два метода: getString: для получения строки с 
консольного ввода printString: для печати строки в верхнем регистре.
"""
class getString:
    def __init__(self, x):
        self.get(x)
        self.print()
    def get(self, a):
        self.a = a
    def print(self):
        print(self.a.upper())
x = getString(input())
