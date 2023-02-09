"""
1. Определите класс, который имеет как минимум два метода: getString: для получения строки с 
консольного ввода printString: для печати строки в верхнем регистре.
"""
class getString:
    def __init__(self, x):
        self.get = x
        self.print()
    def print(self):
        print(self.get.upper())
x = getString(input())