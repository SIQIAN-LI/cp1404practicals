class Project:
    """
    Represents a project with start date, priority, cost estimate and completion percentage.

    Attributes:
    name (str): Project name.
    Start_date (date): Start date as a datetime.date object.
    Priority (int): Smaller value means higher priority.
    Cost_estimate (float): Estimated cost in dollars.
    Completion_percentage (int): Completion percentage in [0, 100].
    """

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialize a Project instance with the given attributes."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a string line used in menus/output."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")

    def __repr__(self):
        """Return a string line used in tests."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Sort projects by priority (smaller number first)."""
        return self.priority < other.priority

    def is_completed(self) -> bool:
        """Return True if the project is completed (>= 100%)."""
        return self.completion_percentage == 100

    def update_percentage(self, new_percentage):
        """Update the completion percentage."""
        self.completion_percentage = new_percentage

    def update_priority(self, new_priority):
        """Update the project priority."""
        self.priority = new_priority
