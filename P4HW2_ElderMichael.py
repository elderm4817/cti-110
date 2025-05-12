# Michael Elder
# 04/26/2025
# P4HW2
# Employee Pay Calculator 

# Constant numbers
standard_hours = 40
overtime_rate = 1.5

# Totals
total_employees = 0
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0

# Ask for employee
employee_name = input("Enter employee's name or 'Done' to terminate: ")

while employee_name != "Done":
    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

    overtime_hours = 0
    overtime_pay = 0
    reghour_pay = 0
    gross_pay = 0

    if hours_worked <= standard_hours:
        reghour_pay = hours_worked * pay_rate
        gross_pay = reghour_pay
    else:
        overtime_hours = hours_worked - standard_hours
        reghour_pay = standard_hours * pay_rate
        overtime_pay = overtime_hours * (pay_rate * overtime_rate)
        gross_pay = reghour_pay + overtime_pay
    
    total_employees += 1
    total_overtime_pay += overtime_pay
    total_regular_pay += reghour_pay
    total_gross_pay += gross_pay


    # the output
    print("Employee name: ",employee_name)
    print(f"\n{'Hours Worked':<15}{'Pay Rate':<15}{'OverTime':<15}{'OverTime Pay':<15}{'RegHour Pay':<15}{'GrossPay':<15}")
    print('------------------------------------------------------------------------------------------------')
    print(f"{hours_worked:<15.2f}${pay_rate:<14.2f}{overtime_hours:<15.2f}${overtime_pay:<14.2f}${reghour_pay:<15.2f}${gross_pay:<14.2f}")

    # Ask for the next employee
    employee_name = input("\nEnter employee's name or 'Done' to terminate: ")

print("\nTotal number of employees entered:", total_employees)
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")