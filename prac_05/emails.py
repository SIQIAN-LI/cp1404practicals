"""
Emails
Estimate: 25 minutes
Actual:   20 minutes
"""
def main():
    email = input("Email: ")
    while email != '':
        name =  extract_name_from_email(email)
        print(name)
        email = input("Email: ")


def extract_name_from_email(email):
    username = email.split('@')[0]
    parts = username.split('.')
    name = ' '.join(parts)
    return name

main()