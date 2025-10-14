"""
Emails
Estimate: 25 minutes
Actual:   20 minutes
"""


def main():
    """Get user's email address and name to print."""
    email_to_name = {}
    email = input("Email: ")
    while email != '':
        name = extract_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").upper()
        if confirmation != 'Y' and confirmation != '':
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name_from_email(email):
    """Get name from email."""
    username = email.split('@')[0]
    parts = username.split('.')
    name = ' '.join(parts)
    return name


main()
