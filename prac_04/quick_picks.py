import random

MAXIMUM_NUMBER = 25
MINIMUM_NUMBER = 1
NUMBER_OF_NUMBERS = 6

number_of_picks = int(input("How many quick picks? "))
for i in range(number_of_picks):
    numbers = []
    while len(numbers) < 6:
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    result = ' '.join([f"{number:>2}" for number in numbers])
    print(result)
