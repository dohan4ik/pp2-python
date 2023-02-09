"""
11. Напишите функцию Python, которая проверяет, является ли слово или фраза 
палиндромом или нет. Примечание: Палиндром - это слово, 
фраза или последовательность, которые читаются одинаково как задом наперед, так и вперед, например, madam
"""
def is_palindrome(string1):
    string1 = string1.lower()
    string2 = ""
    for i in range(len(string1)):
        string2 += string1[len(string1) - (1 + i)]
    if string1 == string2:
        return True
    else:
        return False
string1 = str(input())
print(is_palindrome(string1))