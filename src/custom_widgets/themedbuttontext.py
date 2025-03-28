from typing import List
from kivymd.theming import ThemeManager
from kivy.properties import DictProperty
from kivymd.uix.button import MDButtonText

class ThemedButtonText(MDButtonText):
    texts: List['ThemedButtonText'] = []
    text_colors = DictProperty({'Light': (1, 1, 1, 1), 'Dark': (0, 0, 0, 1)})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.theme_text_color = "Custom"
        ThemedButtonText.texts.append(self)
        self.on_theme_changed()

    def on_theme_changed(self):
        manager: ThemeManager = self.theme_cls

        text_color = self.text_colors.get(manager.theme_style)
        if text_color is not None:
            self.text_color = text_color