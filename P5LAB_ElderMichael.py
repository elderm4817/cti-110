# Michael Elder
# 04/30/2025
# P5LAB
# simulates a self-checkout machine that calculates change and breaks it into dollars and coins.


import random

def disperse_change(change):

    # converts the value to an integer
    change = round(change * 100)

    print(f"Change Amount as integer: ${change}")

    # Determine how many dollars are needed
    dollars = change // 100
    change = change - (dollars * 100)

    quarter = change // 25
    change = change - (quarter * 25)

    dimes = change // 10
    change = change - (dimes *10)

    nickels = change // 5
    change = change - (nickels * 5)

    pennies = change

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



def main():
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe: ${amount_owed:.2f}")

    money = float(input("How much cash will you put in the self-checkout? "))

    change = money - amount_owed
    print(f"Change owed: ${change:.2f}")

    disperse_change(change)

main()