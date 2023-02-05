"""
11. Напишите функцию Python, которая проверяет, является ли слово или фраза 
палиндромом или нет. Примечание: Палиндром - это слово, 
фраза или последовательность, которые читаются одинаково как задом наперед, так и вперед, например, madam
"""
def is_palindrome(string):
    string = string.lower()
    string = string.replace(" ", "")
    return string == string[::-1]

string = input()
print(is_palindrome(string))