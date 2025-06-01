from kivymd.app import MDApp
from kivy.core.window import Window

# custom imports ...
from src.custom.loadthemedwidgets import EventDispatcher
from src.custom.themedwidgtes.themedstyle import ThemedStyle

from src.mainscreenmanager import MainScreenManager

# custom imports database...
from src.database.database import DataBase
from src.database.session import SessionManager

class AppRomaneio(MDApp):
    custom_theme_style = ThemedStyle

    def build(self):
        return MainScreenManager()

    def on_start(self):
        DataBase.init_data_base()

        EventDispatcher.on_update_theme()
        return super().on_start()

    def change_theme(self):
        self.theme_cls.theme_style = "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        
        # fluxo melhor visualmente!
        EventDispatcher.on_update_theme()

    def on_stop(self):
        SessionManager.close_session()

        return super().on_stop()

if __name__ == "__main__":
    # config app...
    Window.size = (320, 600)

    AppRomaneio().run()