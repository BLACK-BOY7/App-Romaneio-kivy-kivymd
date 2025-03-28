from typing import List
from kivymd.theming import ThemeManager

from kivymd.uix.card import MDCard

# custom imports...
from .themedstyle import ThemedStyle

class ThemedCard(MDCard):
    texts: List["ThemedCard"] = []
    background_colors = ThemedStyle.background_primary
    # background_colors = ThemedStyle.background_primary
    shadow_colors = ThemedStyle.background_primary
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.theme_text_color = "Custom"
        ThemedCard.texts.append(self)

        self.on_theme_changed()

    def on_theme_changed(self):
        self.theme_cls: ThemeManager

        text_color = self.background_colors.get(self.theme_cls.theme_style)
        if text_color is not None:
            self.text_color = text_color

    @staticmethod
    def on_update_theme():
        for themed_button_text in ThemedCard.texts:
            themed_button_text.on_theme_changed()