from math import sqrt
def hypotenuse(a, b):
    c = sqrt(a**2 + b**2)
    c = int(c)
    print(f"by using pythagorean theorem hypotenuse size: {c}")
hypotenuse(3, 4)
