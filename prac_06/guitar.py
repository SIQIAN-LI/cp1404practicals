"""
guitar
current time： 3：00
Estimate: 30 minutes
Actual: 20 minutes
"""
CURRENT_YEAR = 2025
VINTAGE_YEAR = 50


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string showing the guitar's details."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the guitar's age in years."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 years or older."""
        return self.get_age() >= VINTAGE_YEAR
