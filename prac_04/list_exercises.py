from prac_01.broken_score import message

numbers = []
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)
max_number = max(numbers)
min_number = min(numbers)
average = sum(numbers) / len(numbers)

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[4]}")
print(f"The smallest number is {min_number}")
print(f"The largest number is {max_number}")
print(f"The average of the numbers is {average}")


