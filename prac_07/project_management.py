from project import Project
from operator import attrgetter
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
            filter_projects(projects)
        elif choice == 'A':
            add_new_project(projects)
        elif choice == 'U':
            update_project(projects)
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


def update_project(projects):
    """Show indexed list, choose a project, then update percentage and/or priority (blank = keep)."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_choice = get_valid_project_choice(projects)
    print(projects[project_choice])
    update_percentage(projects, project_choice)
    update_priority(projects, project_choice)


def get_valid_project_choice(projects):
    """Prompt for a valid project index within [0, len(projects)-1]."""
    maximum_index = len(projects) - 1
    is_valid_input = False
    while not is_valid_input:
        try:
            project_choice = int(input("Project choice: "))
            if project_choice < 0 or project_choice > maximum_index:
                raise ValueError
            is_valid_input = True
        except ValueError:
            print("project choice must between 0 and maximum index")
    return project_choice


def update_percentage(projects, project_choice):
    """Prompt for a new completion percentage; accept blank to leave unchanged."""
    is_valid_input = False
    while not is_valid_input:
        try:
            new_percentage = input("New Percentage: ").strip()
            if new_percentage:
                if int(new_percentage) < 0 or int(new_percentage) > 100:
                    raise ValueError
                projects[project_choice].update_percentage(int(new_percentage))
            is_valid_input = True
        except ValueError:
            print("Percentage must be between 0 and 100 or blank")


def update_priority(projects, project_choice):
    """Prompt for a new priority; accept blank to leave unchanged."""
    is_valid_input = False
    while not is_valid_input:
        try:
            new_priority = input("New Priority: ").strip()
            if new_priority:
                if int(new_priority) <= 0:
                    raise ValueError
                projects[project_choice].update_priority(int(new_priority))
            is_valid_input = True
        except ValueError:
            print("Priority must be larger than 0 or blank")


def add_new_project(projects):
    """Create a new Project from validated user inputs and append to the list."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = get_valid_date_object("Start date (dd/mm/yy): ")
    priority = get_valid_priority("Priority: ")
    cost_estimate = get_valid_cost_estimate("Cost estimate: $")
    completion_percentage = get_valid_percentage("Percent complete: ")
    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(project)


def filter_projects(projects):
    """Ask for a threshold date and display projects that start on/after it (sorted by date)."""
    selected_date = get_valid_date_object("Show projects that start after date (dd/mm/yy): ")
    selected_projects = [project for project in projects if project.start_date >= selected_date]
    for project in sorted(selected_projects, key=attrgetter('start_date')):
        print(project)


def get_valid_date_object(prompt):
    """Prompt until the user enters a valid dd/mm/yyyy (or dd/mm/yy) date; return a date object."""
    is_valid_input = False
    while not is_valid_input:
        try:
            date = input(prompt)
            date_object = datetime.datetime.strptime(date, "%d/%m/%Y").date()
            is_valid_input = True
        except ValueError:
            print("Please match the format (%d/%m/%Y)")
    return date_object


def get_valid_priority(prompt):
    """Prompt until a valid integer priority (> 0) is entered; return the integer."""
    is_valid_input = False
    while not is_valid_input:
        try:
            priority = int(input(prompt))
            if priority <= 0:
                print("Priority must be larger than 0")
            else:
                is_valid_input = True
        except ValueError:
            print("Please input valid number")
    return priority


def get_valid_cost_estimate(prompt):
    """Prompt until a valid non-negative float is entered; return the float."""
    is_valid_input = False
    while not is_valid_input:
        try:
            cost_estimate = float(input(prompt))
            if cost_estimate < 0:
                print("Cost estimate must be larger than 0 or equal to 0")
            else:
                is_valid_input = True
        except ValueError:
            print("Please input a valid number")
    return cost_estimate


def get_valid_percentage(prompt):
    """Prompt until an integer in [0, 100] is entered; return the integer."""
    is_valid_input = False
    while not is_valid_input:
        try:
            completion_percentage = int(input(prompt))
            if completion_percentage < 0 or completion_percentage > 100:
                print("Completion percentage must be between 0 and 100")
            else:
                is_valid_input = True
        except ValueError:
            print("Please input a valid percentage")
    return completion_percentage


main()
