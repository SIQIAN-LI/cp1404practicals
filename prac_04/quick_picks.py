import random

MAXIMUM_NUMBER = 45
MINIMUM_NUMBER = 1
NUMBERS_PER_LINE = 6


def main():
    """Get the number of picks and display these randomly selected numbers in ascending order."""
    number_of_picks = int(input("How many quick picks? "))
    for i in range(number_of_picks):
        random_numbers = generate_quick_pick_per_line()
        random_numbers.sort()
        print(' '.join([f"{number:>2}" for number in random_numbers]))


def generate_quick_pick_per_line():
    """Generate six random and no-repeating numbers in a list."""
    random_numbers = []
    while len(random_numbers) < NUMBERS_PER_LINE:
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        if number not in random_numbers:
            random_numbers.append(number)
    return random_numbers


main()
