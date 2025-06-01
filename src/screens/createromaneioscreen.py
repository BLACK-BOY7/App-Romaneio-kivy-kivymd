from kivy.lang import Builder

from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField

Builder.load_file("src/screens_kv/createromaneioscreen.kv")


class CreateRomaneioScreen(MDScreen):
    def clean_text_fields(self):
        for widget in self.ids.box_layout.children:
            if isinstance(widget, MDTextField):
                widget.text = ""

    def on_pre_enter(self):
        self.clean_text_fields()

    def on_leave(self):
        self.clean_text_fields()