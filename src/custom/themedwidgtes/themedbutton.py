from typing import List
from kivymd.theming import ThemeManager

from kivymd.uix.button import MDButton

# custom imports...
from .themedstyle import ThemedStyle

class ThemedButton(MDButton):
    buttons: List["ThemedButton"] = []
    background_colors = ThemedStyle.background_primary

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.theme_bg_color = "Custom"
        ThemedButton.buttons.append(self)

        self.on_theme_changed()

    def on_theme_changed(self):
        self.theme_cls: ThemeManager
        background_color = self.background_colors[self.theme_cls.theme_style]

        if background_color is not None:
            self.md_bg_color = background_color

    @staticmethod
    def on_update_theme():
        for button in ThemedButton.buttons:
            button.on_theme_changed()