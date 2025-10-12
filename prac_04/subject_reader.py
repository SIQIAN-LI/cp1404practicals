"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"
SUBJECT_INDEX = 0
LECTURER_INDEX = 1
STUDENT_COUNT_INDEX = 2


def main():
    """Read subject data and display concisely."""
    subject_records = load_subject_records(FILENAME)
    display_subjects(subject_records)


def load_subject_records(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer, number of students."""
    subject_records = []
    input_file = open(filename)
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[STUDENT_COUNT_INDEX] = int(parts[STUDENT_COUNT_INDEX])  # Make the number an integer (ignore PyCharm's warning)
        # print(parts)  # See if that worked
        subject_records.append(parts)
        print("----------")
    input_file.close()
    return subject_records


def display_subjects(subject_records):
    """Print subject information neatly."""
    max_name_width, max_number_width = get_alignment_width(subject_records)
    for subject in subject_records:
        print(f"{subject[SUBJECT_INDEX]} is taught by {subject[LECTURER_INDEX]:{max_name_width}} "
              f"and has {subject[STUDENT_COUNT_INDEX]:{max_number_width}} students")


def get_alignment_width(subject_records):
    """Determine the max width of lecturer name and student numbers."""
    max_name_width = max(len(subject[LECTURER_INDEX]) for subject in subject_records)
    max_number_width = max(len(str(subject[STUDENT_COUNT_INDEX])) for subject in subject_records)
    return max_name_width, max_number_width


main()
