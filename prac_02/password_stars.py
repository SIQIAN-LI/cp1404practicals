MINIMUM_LENGTH = 4


def main():
    """Run the password program"""
    password = get_valid_password(MINIMUM_LENGTH)
    print_asterisks(password)


def print_asterisks(password, symbol='*'):
    """Print the asterisks equal to the length of the password"""
    print(len(password) * symbol)


def get_valid_password(minimum_length):
    """Validate the password based on the minimum length"""
    password = input(f"Enter password(at least {minimum_length} characters): ")
    while len(password) < minimum_length:
        print("Invalid password")
        password = input(f"Enter password(at least {minimum_length} characters): ")
    return password


main()
