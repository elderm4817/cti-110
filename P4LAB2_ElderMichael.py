# Michael Elder
# 04/26/2025
# P4LAB2
# Using a while and for loop to make a multiplication table

again = "yes"

while again != "no":
    
    num = int(input('Enter an integer: '))

    if num >=0:
        for item in range (1 ,13):
            print(f"{num} * {item} = {num * item}")

    else:
        print('This program does not handle negative numbers.')

    again = input("Would you like to run the prgram again? ")


print('Exiting program....')