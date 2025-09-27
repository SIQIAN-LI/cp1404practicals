"""
CP1404/CP5632 - Practical
Program to determine score status
"""
EXCELLENT_THRESHOLD = 90
PASSED_THRESHOLD = 50


def main():
    """Get score, determine status, show status."""
    score = float(input("Enter score: "))
    status = determine_status(score)
    print(status)


def determine_status(score):
    """Determine and return the status of a given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= EXCELLENT_THRESHOLD:
        return "Excellent"
    elif score >= PASSED_THRESHOLD:
        return "Pass"
    else:
        return "Bad"


main()
