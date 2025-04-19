# Michael Elder
# 04/18/2025
# P3LAB
# This project is to break down money in its different forms

# Money Breakdown Program

# User is asked to input a value
cents = float(input('Enter the amount of money as a float: $'))

print(f"Change Amount: {cents}")

# converts the value to an integer
cents = round(cents * 100)

print(f"Change Amount: {cents}")

# Determine how many dollars are needed
dollars = cents // 100
cents = cents - (dollars * 100)

quarter = cents // 25
cents = cents - (quarter * 25)

dimes = cents // 10
cents = cents - (dimes *10)

nickels = cents // 5
cents = cents - (nickels * 5)

pennies = cents

if dollars > 0:
    if dollars == 1:
        print(f"{dollars} Dollar")
    else:
        print(f"{dollars} Dollars")

if quarter > 0:
    if quarter == 1:
        print(f"{quarter} Quarters")
    else:
        print(f"{quarter} Quarters")

if dimes > 0:
    if dimes == 1:
        print(f"{dimes} Dimes")
    else:
        print(f"{dimes} Dimes")

if nickels > 0:
    if nickels == 1:
        print(f"{nickels} nickels")
    else:
        print(f"{nickels} nickels")

if pennies > 0:
    if pennies == 1:
        print(f"{pennies} pennies")
    else:
        print(f"{pennies} pennies")



