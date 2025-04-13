# Michael Elder
# 04/12/2025
# P2LAB2
# This project demonstrates the use of dictionaries
car_mpg ={
'Camaro' : 18.21,
'Prius' : 52.36,
'Model S' : 110,
'Silverado' : 26,
}

keys = car_mpg.keys()

print(keys)

car_name = input("Enter a vehicle to see it's mpg: ")


mpg = car_mpg[car_name]

print(f"The {car_name} gets {mpg} miles per gallon.")

miles = float(input(f"How many miles will you drive the {car_name}?: "))

gallons_needed = miles / mpg

print(f"You will need approximately {gallons_needed:.2f} gallons of gas to drive {miles} miles in the {car_name}.")