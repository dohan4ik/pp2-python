"""
3.Напишите программу для решения классической головоломки: Мы насчитали 35 голов и 94 ноги у цыплят и кроликов на ферме. 
Сколько у нас кроликов и сколько кур? Создайте функцию: solve(numheads, numlegs):
"""
heads = int(input())
legs = int(input())
def my_finction(heads, legs):
    y = ((4 * heads) - legs) / 2
    x = 35 - y
    return x, y
print(my_finction(heads, legs))