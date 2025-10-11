# Basic list operations
NUMBERS_COUNT = 5

numbers = []
for i in range(NUMBERS_COUNT):
    number = int(input("Number: "))
    numbers.append(number)
max_number = max(numbers)
min_number = min(numbers)
average = sum(numbers) / len(numbers)

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min_number}")
print(f"The largest number is {max_number}")
print(f"The average of the numbers is {average}")

# Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
             'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command',
             'ExecState', 'InteractiveConsole', 'InterpreterInterface',
             'StartServer', 'bob']

username = input("Enter your username: ")
if username in usernames:
    message = "Access granted"
else:
    message = "Access denied"
print(message)
