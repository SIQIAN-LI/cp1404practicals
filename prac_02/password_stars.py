MINIMUM_LENGTH = 4


def main():
    """Run the password program"""
    password = get_valid_password()
    print_asterisks(password)


def print_asterisks(password, symbol='*'):
    """Print the asterisks equal to the length of the password"""
    print(len(password) * symbol)


def get_valid_password():
    """Validate the password"""
    password = input(f"Enter password(at least {MINIMUM_LENGTH} characters): ")
    while len(password) < MINIMUM_LENGTH:
        print("Invalid password")
        password = input(f"Enter password(at least {MINIMUM_LENGTH} characters): ")
    return password


main()
