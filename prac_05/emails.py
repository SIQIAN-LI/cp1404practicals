"""
Emails
Estimate: 25 minutes
Actual:   20 minutes
"""


def main():
    key_to_values = {}
    email = input("Email: ")
    while email != '':
        name = extract_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").upper()
        if confirmation != 'Y' and confirmation != '':
            name = input("Name: ")

        key_to_values[email] = name
        email = input("Email: ")
    print(key_to_values)

def extract_name_from_email(email):
    username = email.split('@')[0]
    parts = username.split('.')
    name = ' '.join(parts)
    return name


main()
