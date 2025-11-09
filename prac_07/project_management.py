from project import Project
import datetime

MENU = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n"
        "- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit")
DEFAULT_FILENAME = 'projects.txt'


def main():
    projects = load_projects(DEFAULT_FILENAME)
    print(projects)
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'L':
            pass
        elif choice == 'S':
            pass
        elif choice == 'D':
            pass
        elif choice == 'F':
            pass
        elif choice == 'A':
            pass
        elif choice == 'U':
            pass
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()


def load_projects(filename):
    """Load projects from a tab-delimited file."""
    projects = []
    with open(filename, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            name, start_date, priority, cost_estimate, percentage = line.strip().split('\t')
            date_object = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
            project = Project(name, date_object, int(priority), float(cost_estimate), int(percentage))
            projects.append(project)
    return projects


main()
