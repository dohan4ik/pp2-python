# !!!!! Python Lists  !!!!! #
# 1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
# 2
fruits["apple", "banana", "cherry"]
fruits[0] = "kiwi" 
# 3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
# 4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
# 5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
# 6
fruits = ["apple", "banana", " cherry"]
print(fruits[-1])
# 8 
fruits["apple", "banana", "cherry", "orage", "kiwi", "melon", "mango"]
print(fruits[2:5])
# !!!!! Python Tuples  !!!!! #
# 1
fruits = ("apple", "banana", "cherry")
print(fruits[0])
# 2
fruits = ("apple", "banana", "cherry")
print(len(fruits))
# 3
fruits = ("apple", "banana", "cherry")
print(fruits[-1])
# 4
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])
# !!!!! Python Sets  !!!!! #
# 1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("Yes, apple is a fruit!")
# 2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
# 3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
# 4 
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
# 5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
# !!!!! Python While Loops  !!!!! #
# 1
i = 1
while i < 6:
    print(i)
    i += 1
# 2
i = 1
while i < 6:
    if i == 3:
        break
    i += 1
# 3
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
# 4
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
# !!!!! Python For Loops  !!!!! #
# 1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
# 2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
# 3
for x in range(6):
    print(x)
# 4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)
# !!!!! Python Dictionaries  !!!!! #
# 1 
car =   {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(car.get("model"))
# 2
car =   {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car["year"] = 2020
# 3
car =   {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car["color"] = "red"
# 4 
car =   {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car.pop("model")
# 5 
car =   {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car.clear()
# !!!!! Python Arrays  !!!!! #