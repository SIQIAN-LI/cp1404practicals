"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {
                "QLD": "Queensland",
                "NSW": "New South Wales",
                "NT": "Northern Territory",
                "WA": "Western Australia",
                "ACT": "Australian Capital Territory",
                "VIC": "Victoria",
                "TAS": "Tasmania", "SA": "South Australia"
}

print(CODE_TO_NAME)
max_state_code_width = max(len(state_code) for state_code in CODE_TO_NAME.keys())
state_code = input("Enter short state: ").strip().upper()
while state_code != "":
    try:
        print(f"{state_code:{max_state_code_width}} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").strip().upper()
