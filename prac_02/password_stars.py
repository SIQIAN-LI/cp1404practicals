password = input("Enter your password: ")
while len(password) < 4:
    print("Your password must be at least 4 characters long")
    password = input("Enter your password: ")
print(len(password) * '*')
