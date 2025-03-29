from typing import List
from kivymd.theming import ThemeManager

from kivymd.uix.label import MDIcon

# custom imports...
from .themedstyle import ThemedStyle

class ThemedIcon(MDIcon):
    icons: List["ThemedIcon"] = []
    icon_colors = ThemedStyle.icon_color_primary
    # background_colors = ThemedStyle.background_primary
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.theme_icon_color = "Custom"
        # self.theme_bg_color = "Custom"
        ThemedIcon.icons.append(self)

        self.on_theme_changed()

    def on_theme_changed(self):
        self.theme_cls: ThemeManager
        icon_color = self.icon_colors.get(self.theme_cls.theme_style)
        # background_color = self.background_colors.get(self.theme_cls.theme_style)

        if icon_color is not None:
            self.icon_color = icon_color

        # if background_color is not None:
        #     self.md_bg_color = background_color

    @staticmethod
    def on_update_theme():
        for themed_card in ThemedIcon.icons:
            themed_card.on_theme_changed()