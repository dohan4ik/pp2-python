# !!!!! Python Syntax !!!!! #
# 1
print("Hello World")
# 2
if 5 > 2:
    print("Five is greater than two!")
# !!!!! Python Comments !!!!! #
# 1
# this is a comment
# 2
"""
This is a comment written in more that just one line
"""
# !!!!! Python Variables !!!!! #
# 1
carName = "Volvo"
# 2
x = 50
# 3
x = 5
y = 10
print(x + y)
# 4
x = 5
y = 10
z = x + y
print(z)
# 5
myfirst_name = "John"
# 6
x = y = z = "Orange"
# 7
def myfunc():
    global x
    x = "fantastic"
# !!!!! Python Data Types !!!!! #
# 1
x = 5
print(type(x))  # int
# 2
x = "Hello World"
print(type(x))  # str
# 3
X = 20.5
print(type(x))  # float
# 4
x = ["apple", "banana", "cherry"]
print(type(x))  # list
# 5
x = ("apple", "banana", "cherry")
print(type(x))  # tuple
# 6
x = {"name": "John", "age": 36}
print(type(x))  # dict
# 7
x = True
print(type(x))  # bool
# !!!!! Python Numbers !!!!! #
# 1
x = 5
x = float(x)
# 2
x = 5.5
x = int(x)
# 3
x = 5
x = complex(x)
# !!!!! Python Strings !!!!! #
# 1
x = "Hello World"
print(len(x))
# 2
txt = "Hello World"
x = txt[0]
# 3
txt = "Hello World"
x = txt[2:5]
# 4
txt = " Hello World "
x = txt.strip()
# 5
txt = "Hello World"
txt = txt.upper()
# 6
txt = "Hello World"
txt = txt.lower()
# 7
txt = "Hello World"
txt = txt.replace("H", "J")
# 8
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
# !!!!! Python Booleans !!!!! #
# 1
print(10 > 9)  # True
# 2
print(10 == 9)  # False
# 3
print(10 < 9)  # False
# 4
print(bool("abc"))  # True
# 5
print(bool(0))  # False
# !!!!! Python Operators !!!!! #
# 1
print(10 * 5)
# 2
print(10 / 2)
# 3
fruits = ["apple", "banana"]
if "apple" in fruits:
    print("Yes, apple is aa fruits!")
# 4
if 5 != 10:
    print("5 and 10 is not equal")
# 5
if 5 == 10 or 4 == 4:
    print("At least one of the statements is true")
