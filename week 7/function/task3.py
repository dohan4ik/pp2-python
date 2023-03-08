def is_palindrom(text):
    if text == text[::-1]:
        return True
    else:
        return False
a = input()
is_palindrom(a)
if is_palindrom(a) == True:
    print("Is polindrom!")
else:
    print("Is not polindrom.")
