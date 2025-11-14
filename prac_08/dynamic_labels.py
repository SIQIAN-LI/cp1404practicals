from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """A simple Kivy app that creates labels dynamically from a list of names."""

    def __init__(self, **kwargs):
        """Initialise the app and define the list of names."""
        super().__init__(**kwargs)
        self.names = ["Enzo", "Jack", "Rose", "Brown"]

    def build(self):
        """Build the app interface and add labels for each name."""
        self.title = 'Dynamic Labels'
        self.root = Builder.load_file('dynamic_labels.kv')
        for name in self.names:
            added_label = Label(text=name)
            added_label.color = (1, 1, 0, 1)
            self.root.ids.name_labels.add_widget(added_label)
        return self.root


DynamicLabelsApp().run()
