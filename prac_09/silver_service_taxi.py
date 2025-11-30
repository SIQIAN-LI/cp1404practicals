from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """A Taxi with higher price_per_km scaled by fanciness and an extra flagfall charge."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi, scaling price_per_km by fanciness."""
        super().__init__(name, fuel)
        self.price_per_km *= fanciness

    def __str__(self):
        """Return string with parent details plus flagfall info."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return fare including the base fare and the extra flagfall charge."""
        return super().get_fare() + self.flagfall
