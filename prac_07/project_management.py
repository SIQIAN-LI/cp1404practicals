from project import Project
import datetime

MENU = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n"
        "- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit")
DEFAULT_FILENAME = 'projects.txt'


def main():
    projects = load_projects(DEFAULT_FILENAME)
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
            display_projects(projects)
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
    choice = input("Would you like to save to projects.txt? ").upper()
    if choice == 'Y':
        save_projects(DEFAULT_FILENAME, projects)
    print("Thank you for using custom-built project management software.")


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


def save_projects(filename, projects):
    """Save the current projects to a tab-delimited file with a header row."""
    with open(filename, 'w') as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage")
        for project in projects:
            out_file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t"
                           f"{project.cost_estimate}\t{project.completion_percentage}\n")


def display_projects(projects):
    """Display incomplete and completed groups, each group sorted by priority."""
    completed_projects = sorted(project for project in projects if project.is_completed())
    incomplete_projects = sorted(project for project in projects if not project.is_completed())
    print("Incomplete projects:")
    for project in incomplete_projects:
        print(project)
    print("Completed projects:")
    for project in completed_projects:
        print(project)


main()
