"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
# TODO: Fix this!
LOWEST_SCORE = 0
HIGHEST_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASSABLE_THRESHOLD = 50

score = float(input("Enter score: "))
if score < LOWEST_SCORE or score > HIGHEST_SCORE:
    message = "Invalid score"
elif score >= EXCELLENT_THRESHOLD:
    message = "Excellent"
elif score >= PASSABLE_THRESHOLD:
    message = "Passable"
else:
    message = "Bad"
print(message)