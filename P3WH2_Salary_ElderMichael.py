# Michael Elder
# 04/18/2025
# P3WH2
# This project is a salary calculator that uses branching

# Order of operation
    # 1. asked to input name, hours worked, and employee rate
    # 2. some definitions are defined and defaul values are set for if the worker does not work overtime
    # 3. the branching logic is defined and set up to correctly make the calculations
    # 4. the output is formatted in a way that is easily readable and will provide the proper calculations 

# iputs the information needed to make the calculations
var1 = input("Enter employee's name: ")
var2 = float(input("Enter number of hours worked: "))
var3 = float(input("Enter employee's pay rate: "))

# Constant numbers
standard_hours = 40
overtime_rate = 1.5
hours_worked = var2
pay_rate = var3

# Default values 
overtime_hours = 0
overtime_pay = 0
reghour_pay = 0
gross_pay = 0


# Logic
if var2 <= standard_hours:  # Calcuate the amount owed to the employee for overtime, They should receive 1.5 times their normal pay rate for overtimed hours
    reghour_pay = var2 * var3
    gross_pay = reghour_pay
  
else:
    overtime_hours = var2 - standard_hours
    reghour_pay = standard_hours * var3
    overtime_pay = overtime_hours * (var3 * overtime_rate)
    gross_pay = reghour_pay + overtime_pay
print('-------------------------------------------')

# the output
print("Employee name: ",var1)
print(f"\n{'Hours Worked':<15}{'Pay Rate':<15}{'OverTime':<15}{'OverTime Pay':<15}{'RegHour Pay':<15}{'GrossPay':<15}")
print('------------------------------------------------------------------------------------------------')
print(f"{hours_worked:<15.2f}${pay_rate:<14.2f}{overtime_hours:<15.2f}${overtime_pay:<14.2f}${reghour_pay:<15.2f}${gross_pay:<14.2f}")
