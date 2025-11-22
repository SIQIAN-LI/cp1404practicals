class Band:
    """Represent a Band that has a name and a list of musician members."""
    def __init__(self, name):
        self.name = name
        self.members = []

    def __str__(self):
        """Initialise a Band with a name and an empty list of members."""
        return f"{self.name} ({', '.join([str(member) for member in self.members])})"

    def play(self):
        """Return a string showing each member playing their first instrument."""
        return "\n".join([member.play() for member in self.members])

    def add(self, member):
        """Add a musician to the band."""
        self.members.append(member)
