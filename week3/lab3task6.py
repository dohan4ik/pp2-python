"""
6.Напишите функцию, которая принимает строку 
от пользователя и возвращает предложение с обратными словами. 
Мы готовы -> Мы готовы
"""
def reverse(sentence):
    word = sentence.split()
    word.reverse()
    return ' '.join(word)
x = input()
print(reverse())