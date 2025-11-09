from guitar import Guitar

FILENAME = 'guitars.csv'


def main():
    """Load existing guitars and get new guitars, display all guitars in order, then save to file."""
    guitars = load_file(FILENAME)
    new_guitars = get_guitars()
    guitars += new_guitars
    guitars.sort()
    print()
    print("Guitars:")
    for guitar in guitars:
        print(guitar)
    save_guitars(FILENAME, guitars)


def load_file(filename):
    """Load existing guitars' information from file."""
    guitars = []
    with open(filename, 'r') as in_file:
        guitar_data = [line.strip().split(',') for line in in_file]
        for name, year, cost in guitar_data:
            guitar = Guitar(name, int(year), float(cost))
            guitars.append(guitar)
    return guitars


def get_guitars():
    """Get guitar objects by user input and store them in a list."""
    guitars = []
    guitar_name = input("Name: ")
    while guitar_name != '':
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: $"))
        guitar = Guitar(guitar_name, int(guitar_year), float(guitar_cost))
        guitars.append(guitar)
        print(f"{guitar} added.")
        guitar_name = input("Name: ")
    return guitars


def save_guitars(filename, guitars):
    """Save guitars to file."""
    with open(filename, 'w', newline='') as out_file:
        for guitar in guitars:
            out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


main()
