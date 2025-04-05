# Michael Elder
# 04/05/2025
# P1HW1
# This project demonstrates the input and print function in addition to python ability to do different mathematical equations with the addition of human input.
print('-----Calculating Exponenets-----')

base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter and integer as the exponenet: "))

result = base ** exponent

print(base, "raised to the power of", exponent, "is", result, "!!")

print('-----Addition and Subtracting-----')

int_start = int(input("Enter a starting integear: "))
int_add = int(input("Enter an integear to add: "))
int_sub = int(input("Enter a integearto subtract: "))

result = int_start + int_add - int_sub

print(int_start, "+", int_add, "-", int_sub, "is equal to", result)