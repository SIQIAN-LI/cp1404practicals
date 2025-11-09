from guitar import Guitar

FILENAME = 'guitars.csv'


def main():
    guitars = load_file()
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def load_file():
    guitars = []
    with open(FILENAME, 'r') as in_file:
        guitar_data = [line.strip().split(',') for line in in_file]
        for name, year, cost in guitar_data:
            guitar = Guitar(name, year, float(cost))
            guitars.append(guitar)
    return guitars


main()
