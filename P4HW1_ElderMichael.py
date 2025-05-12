# Michael Elder
# 04/26/2025
# P4HW1
# Analyze the scores inputted 


# 1. Ask the user how many scores they want to enter

# 2. Create an empty list to store scores

# 3. For the scores the user wants to enter:
    # a. Ask the user to enter the score
    # a. While the score entered is invalid
        # i. Show an error message
        # ii. Ask the user to enter the score again
    # a. Add the valid score to the list

# 4. Find and remove the lowest score in the list

# 5. Remove the lowest score from the list

# 6. Calcute the average of the remaining scores

# 7. Determine the letter grade based on teh average 

# 8. Display the results

# Ask how many scores 
scores = int(input("How many scores would you like to enter? "))


# Empty list to store the scores
scores_list = []

# Get the scores
for grade in range(scores):
    score = float(input(f"Enter score #{grade+1}: "))

    # Check if it's a valid score
    while score < 0 or score >100:
        print("Invalid score! Must be between 0 and 100.")
        score = float(input(f"Enter score #{grade+1} again: "))

    scores_list.append(score)

# Find and remove the lowest score
lowest = min(scores_list)
scores_list.remove(lowest)

# Find the average
average = sum(scores_list) / len(scores_list)


# Find the letter grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

# Show the results
print("\n------------Results------------")
print(f"Lowest Score  : {lowest}")
print(f"Modified List : {scores_list}")
print(f"Scores Average: {average:.2f}")
print(f"Grade         : {grade}")
print("------------------------------")