"""
9. Write a function that computes the volume of a sphere given its radius.
"""
def my_function(radius):
    return 4/3 * 3.14 * (radius ** 3)
radius = int(input())
volume = my_function(radius)
print("The volume is %.2f" % volume)