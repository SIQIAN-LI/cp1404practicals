"""
Wimbledon
Estimate: 25 minutes
Actual:   20 minutes
"""
FILENAME = "wimbledon.csv"


def main():
    records = load_records(FILENAME)
    print(records)


def load_records(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        records = [record.strip().split(',') for record in in_file.readlines()]
    return records


main()
