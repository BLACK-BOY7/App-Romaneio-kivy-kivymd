from kivy.lang import Builder
from kivymd.uix.screenmanager import MDScreenManager

# custom imports...
from src.custom_widgets.appbar import  CustomTopAppBar

Builder.load_file("src/mainscreenmanager.kv")


class MainScreenManager(MDScreenManager):
    def change_screen(self, screen_name: str, direction="left", duration=0.2):
        self.current = screen_name
        self.transition.duration = duration
        self.transition.direction = direction