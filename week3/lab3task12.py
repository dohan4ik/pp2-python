"""
12. Define a functino histogram() that takes a list of integers and prints a histogram to the screen. 
For example, histogram([4, 9, 7]) should print the following:
12. Определите функцию histogram(), которая принимает список целых чисел и выводит гистограмму на экран. 
Например, histogram([4, 9, 7]) должна вывести следующее:
"""
def histogram(l):
    data = l.split()
    for value in data:
        x = []
        i = 0
        while i < value:
            x.append("*")
            i += 1
        print(x)


l = list(input())
histogram(l)