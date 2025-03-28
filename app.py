from kivymd.app import MDApp
from kivy.core.window import Window
from src.custom_widgets.themedbutton import ThemedButton
from src.custom_widgets.themedbuttontext import ThemedButtonText

# custom import ...
from src.mainscreenmanager import MainScreenManager

class AppRomaneio(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return MainScreenManager()

    def change_theme(self):
        self.theme_cls.theme_style = "Dark" if self.theme_cls.theme_style == "Light" else "Light"

        for button in ThemedButton.buttons:
            button.on_theme_changed()

        for text in ThemedButtonText.texts:
            text.on_theme_changed()

if __name__ == "__main__":
    
    # config app...
    Window.size = (320, 600)

    AppRomaneio().run()