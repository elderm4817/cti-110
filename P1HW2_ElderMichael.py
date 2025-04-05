# Michael Elder
# 04/05/2025
# P1HW2
# This project is used to calculate travel expenses and subtract it from the budget given to allow a quick and tidy response.
# program Pseudocode (logic)

print("This program calculates and displays travel expenses")

budget = int(input('Enter Budget: '))
dst = input('Enter your travel destination: ')
gas = int(input('How much do you think you will spend on gas?: '))
acc = int(input('Approximately, how much will you spend on accommodations?: '))
food = int(input('How much do you think you will spend on food?: '))

expenses = gas + acc + food

result = budget - expenses

print("------------Travel Expenses------------")
print("Location:", dst)
print("Initial Budget:", budget,"\n")

print("Gas:", gas)
print("Accomodation:", acc)
print("Food:", food, "\n")

print("Remaining Balance:", result)