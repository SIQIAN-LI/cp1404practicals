"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    When input is not an integer number

2. When will a ZeroDivisionError occur?
    When denominator inputted by user is 0

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Use while loop to do error-checking
"""
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator can't be zero")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
