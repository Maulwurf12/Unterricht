'''from math import pi
def calculateArea(radius):
    return pi * (radius**2)
def calculateCircumference(radius):
    return 2 * pi * radius'''

#better circle.py
from math import pi

def calculateArea(radius):
    if not isinstance(radius, (int, float)):
        raise ValueError("Radius must be a number")
    if radius < 0:
        raise TypeError("Radius cannot be negative")
    return pi * (radius**2)

def calculateCircumference(radius):
    if not isinstance(radius, (int, float)):
        raise ValueError("Radius must be a number")
    if radius < 0:
        raise TypeError("Radius cannot be negative")
    return 2 * pi * radius