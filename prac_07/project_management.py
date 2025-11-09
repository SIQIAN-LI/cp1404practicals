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


main()
