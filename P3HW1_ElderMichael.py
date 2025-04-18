# Michael Elder
# 04/17/2025
# P3WH1
# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
sum = sum(grades)
avg = sum / len(grades)

# Puts the grades in order 

print("\n------------Results------------")
print(f"Lowest Grade:        {low}")
print(f"Highest Grade:       {high}")
print(f"Sum of Grades:       {sum}")
print(f"Average:             {avg:.2f}")
print("------------------------------------------")

# Determines the letter grade for average

if avg >= 90:
    print('Your grade is: A')


elif avg > 80:
    print('Your grade is: B')

else:
    print('Your grade is: F') 





