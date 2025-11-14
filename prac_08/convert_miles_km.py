from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """A simple Kivy app that converts miles to kilometres."""
    converted_distance = StringProperty()

    def build(self):
        """Build the app interface and load the KV file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """Handle the conversion from miles to kilometres."""
        value = self.get_validated_miles()
        self.converted_distance = str(value * MILES_TO_KM)

    def handle_increment(self, change):
        """Increase or decrease the miles value by the given change."""
        value = self.get_validated_miles()
        self.root.ids.input_miles.text = str(value + change)

    def get_validated_miles(self):
        """Return the miles value as a float, or 0 if input is invalid."""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesConverterApp().run()
