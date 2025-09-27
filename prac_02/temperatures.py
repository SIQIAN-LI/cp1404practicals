"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""
CELSIUS_TO_FAHRENHEIT_FACTOR = 9.0 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5.0 / 9
FAHRENHEIT_OFFSET = 32
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """Display menu, get choice, convert temperature, show result."""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit : "))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + FAHRENHEIT_OFFSET
    return fahrenheit


def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - FAHRENHEIT_OFFSET)
    return celsius


main()
