"""
Wimbledon
Estimate: 25 minutes
Actual:   20 minutes
"""
FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    records = load_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_result(champion_to_count, countries)


def display_result(champion_to_count, countries):
    print("Wimbledon Champions: ")
    for name, count in champion_to_count.items():
        print(f"{name} {count}")
    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(', '.join(sorted(countries)))


def load_records(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        records = [record.strip().split(',') for record in in_file.readlines()]
    return records


def process_records(records):
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[COUNTRY_INDEX])
        champion_to_count[record[CHAMPION_INDEX]] = champion_to_count.get(record[CHAMPION_INDEX], 0) + 1
    return champion_to_count, countries


main()
