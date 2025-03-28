from typing import List
from kivymd.uix.button import MDButton
from kivymd.theming import ThemeManager
from kivy.properties import DictProperty

class ThemedButton(MDButton):
    buttons: List['ThemedButton'] = []
    background_colors = DictProperty({'Light': (0, 0, 0, 1), 'Dark': (1, 1, 1, 1)})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.theme_bg_color = "Custom"
        ThemedButton.buttons.append(self)
        self.on_theme_changed()

    def on_theme_changed(self):
        manager: ThemeManager = self.theme_cls

        print(manager.theme_style)
        background_color = self.background_colors.get(manager.theme_style)
        print(background_color)
        if background_color is not None:
            self.md_bg_color = background_color