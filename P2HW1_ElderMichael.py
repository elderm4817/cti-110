# Michael Elder
# 04/12/2025
# P2HW1
# This project demonstrates formatting variables

print("This program calculates and displays travel expenses")

budget = float(input('Enter Budget: '))
dst = input('Enter your travel destination: ')
gas = float(input('How much do you think you will spend on gas?: '))
acc = float(input('Approximately, how much will you spend on accommodations?: '))
food = float(input('How much do you think you will spend on food?: '))

expenses = gas + acc + food

result = budget - expenses

print("\n------------Travel Expenses------------")
print(f"Location:            {dst}")
print(f"Initial Budget:      ${budget:.2f}")
print(f"Fuel:                ${gas:.2f}")
print(f"Accomodation:        ${acc:.2f}")
print(f"Food:                ${food:.2f}")
print("---------------------------------------\n")
print(f"Remaining Balance    ${result:.2f}")