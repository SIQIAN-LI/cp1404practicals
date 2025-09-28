"""
The menu should have four separate options:
(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit
"""
EXCELLENT_THRESHOLD = 90
PASSABLE_THRESHOLD = 50
LOWEST_SCORE = 0
HIGHEST_SCORE = 100
MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    """Display a menu to get score, print result, show stars, or quit."""
    score = get_valid_score(LOWEST_SCORE, HIGHEST_SCORE)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score(LOWEST_SCORE, HIGHEST_SCORE)
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")


def get_valid_score(lowest_score, highest_score):
    """Prompt for a valid score (0–100) and return it."""
    score = int(input("Score: "))
    while score > highest_score or score < lowest_score:
        print("Invalid score")
        score = int(input("Score: "))
    return score


def print_result(score):
    """Print the result of a given score."""
    print(determine_result(score))


def determine_result(score):
    """Determine and return the result of a given score."""
    if score >= EXCELLENT_THRESHOLD:
        return "Excellent"
    elif score >= PASSABLE_THRESHOLD:
        return "Passable"
    else:
        return "Bad"


def show_stars(score, symbol='*'):
    """Display the stars based on the given score."""
    print(symbol * score)


main()
