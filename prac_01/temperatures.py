"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
CELSIUS_TO_FAHRENHEIT_FACTOR = 9.0 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5.0 / 9
FAHRENHEIT_OFFSET = 32
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + FAHRENHEIT_OFFSET
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        # TODO: Write this section to convert F to C and display the result
        fahrenheit = float(input("Fahrenheit : "))
        celsius = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - FAHRENHEIT_OFFSET)
        print(f"Result: {celsius:.2f} C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")



