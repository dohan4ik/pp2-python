"""
13. Напишите программу, способную играть в игру "Угадай число", где число, которое нужно угадать, выбирается случайным образом между 1 и 20. Вот как она должна работать при запуске в терминале:
    Привет! Как вас зовут?
    KBTU

    Ну, KBTU, я думаю о числе от 1 до 20.
    Угадай.
    12

    Ваше число слишком мало.
    Угадай.
    16

    Ваше предположение слишком низкое.
    Угадайте.
    19
"""
import random
def guess_the_number():
    print("Hello! What is your name?\n")
    name = input()
    print("Well, %s, I am thinking of a number between 1 and 20." % name)
    number = random.randint(1, 20)
    guess = None
    guess_count = 0

    while guess != number:
        print("Take a guess.")
        guess = int(input())
        guess_count += 1

        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")

    print("Good job, %s! You guessed my number in %i guesses." % (name, guess_count))


guess_the_number()