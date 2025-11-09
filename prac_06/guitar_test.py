from guitar import Guitar

gibson_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another Guitar", 2013, 1500)

print(f"{gibson_guitar.name} get_age() - Expected 103. Got {gibson_guitar.get_age()}")
print(f"{another_guitar.name} get_age() - Expected 12. Got {another_guitar.get_age()}")
print(f"{gibson_guitar.name} is_vintage() - Expected True. Got {gibson_guitar.is_vintage()}")
print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")


