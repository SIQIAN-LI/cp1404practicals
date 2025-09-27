MINIMUM_LENGTH = 4


def main():
    password = get_valid_password()
    symbol = input("Enter a symbol(default is *): ")
    print_asterisks(password)


def print_asterisks(password, symbol='*'):
    print(len(password) * symbol)


def get_valid_password():
    password = input(f"Enter password(at least {MINIMUM_LENGTH} characters): ")
    while len(password) < MINIMUM_LENGTH:
        print("Invalid password")
        password = input(f"Enter password(at least {MINIMUM_LENGTH} characters): ")
    return password


main()
