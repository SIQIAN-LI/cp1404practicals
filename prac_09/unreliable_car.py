from prac_09.car import Car
from random import uniform


class UnreliableCar(Car):
    """Car that only drives based on its reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise the car with reliability."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string showing the car details plus its reliability percentage."""
        return f"{super().__str__()}, reliability={self.reliability}"

    def drive(self, distance):
        """Drive only if random check is below reliability."""
        distance_driven = 0
        if uniform(0, 100) < self.reliability:
            distance_driven = super().drive(distance)
        return distance_driven
