# Michael Elder
# 04/12/2025
# P2Lab1
# This project is to demonstrate mathematical equations in python as well as using arithmetic expressions.

import math

radius = float(input("Please enter the Radius: "))

cir = 2 * math.pi * radius
diam = 2 * radius
area = math.pi * (radius ** 2)

print("\n----- Circle Calculations -----")

print(f"The Diameter is {diam:.1f}")
print(f"The Area is {area:.3f}")
print(f"The Circumference is {cir:.2}")
