from kivymd.app import MDApp
from kivy.core.window import Window

# custom import ...
from src.custom.loadthemedwidgets import EventDispatcher
from src.custom.themedwidgtes.themedstyle import ThemedStyle

from src.mainscreenmanager import MainScreenManager


class AppRomaneio(MDApp):
    custom_theme_style = ThemedStyle

    def build(self):
        return MainScreenManager()

    def on_start(self):
        EventDispatcher.on_update_theme()
        return super().on_start()

    def change_theme(self):
        self.theme_cls.theme_style = "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        
        # fluxo melhor visualmente!
        EventDispatcher.on_update_theme()

if __name__ == "__main__":
    # config app...
    Window.size = (320, 600)

    AppRomaneio().run()