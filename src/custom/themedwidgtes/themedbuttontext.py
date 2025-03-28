from typing import List
from kivymd.theming import ThemeManager

from kivymd.uix.button import MDButtonText

# custom imports...
from .themedstyle import ThemedStyle

class ThemedButtonText(MDButtonText):
    texts: List["ThemedButtonText"] = []
    text_colors = ThemedStyle.text_color_primary
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.theme_text_color = "Custom"
        ThemedButtonText.texts.append(self)

        self.on_theme_changed()

    def on_theme_changed(self):
        self.theme_cls: ThemeManager
        text_color = self.text_colors.get(self.theme_cls.theme_style)

        if text_color is not None:
            self.text_color = text_color

    @staticmethod
    def on_update_theme():
        for themed_button_text in ThemedButtonText.texts:
            themed_button_text.on_theme_changed()