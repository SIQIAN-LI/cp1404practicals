"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random

LOWEST_SCORE = 0
HIGHEST_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASSABLE_THRESHOLD = 50


def main():
    """Get score and random score, determine their status, show their status."""
    score = float(input("Enter score: "))
    status = determine_status(score)
    print(status)
    random_score = random.randint(LOWEST_SCORE, HIGHEST_SCORE)
    status = determine_status(random_score)
    print(f"status of random score {random_score} is {status}")


def determine_status(score):
    """Determine and return the status of a given score."""
    if score < LOWEST_SCORE or score > HIGHEST_SCORE:
        return "Invalid score"
    elif score >= EXCELLENT_THRESHOLD:
        return "Excellent"
    elif score >= PASSABLE_THRESHOLD:
        return "Passable"
    else:
        return "Bad"


main()
