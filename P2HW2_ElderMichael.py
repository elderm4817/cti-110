# Michael Elder
# 04/12/2025
# P2HW2
# This project takes multiple grades from the user, stores them, and then displays the lowest, highest, total, and average grades.

# Pseudocode:
# 1. The user is prompted to input grades of each module
# 2. Store each grade in a list called grades.
# 3. Use functions to calculate:
#     - Lowest grade
#     - Highest grade
#     - Sum of grades
#     - Average of grades (sum divided by number of grades)
# 4. The results are displayed with appropriate labels and formatting.
#     - Average should display two decimal places

m1 = float(input('Enter grade for Module 1: '))
m2 = float(input('Enter grade for Module 2: '))
m3 = float(input('Enter grade for Module 3: '))
m4 = float(input('Enter grade for Module 4: '))
m5 = float(input('Enter grade for Module 5: '))
m6 = float(input('Enter grade for Module 6: '))

grades = [m1, m2, m3, m4, m5, m6]

lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total / len(grades)

print("\n------------Results------------")
print(f"Lowest Grade:        {lowest}")
print(f"Highest Grade:       {highest}")
print(f"Sum of Grades:       {total}")
print(f"Average:             {average:.2f}")
print("------------------------------")