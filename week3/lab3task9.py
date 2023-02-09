"""
9. Write a function that computes the volume of a sphere given its radius.
4p(r)*3/3
"""
def my_volume(radius):
    return (4 * 3.14 * (radius ** 3))/3
radius = int(input())
print(my_volume(radius))