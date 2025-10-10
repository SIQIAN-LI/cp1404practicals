"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Read subject data and display concisely."""
    subject_records = load_data(FILENAME)
    print(subject_records)
    display_subjects(subject_records)



def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer, number of students."""
    subject_records = []
    input_file = open(filename)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        subject_records.append(parts)
        print("----------")
    input_file.close()
    return subject_records


def display_subjects(subject_records):
    """Print subject information neatly."""
    max_name_width, max_number_width = determine_alignment(subject_records)
    for subject in subject_records:
        print(f"{subject[0]} is taught by {subject[1]:<{max_name_width}} and has {subject[2]:>{max_number_width}} students")


def determine_alignment(subject_records):
    """Determine the max width of lecturer name and student numbers."""
    max_name_width = max(len(subject[1]) for subject in subject_records)
    max_number_width = max(len(str(subject[2])) for subject in subject_records)
    return max_name_width, max_number_width


main()
