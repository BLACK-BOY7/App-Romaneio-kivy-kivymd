from kivymd.app import MDApp
from kivy.core.window import Window


# custom import ...
from src.mainscreenmanager import MainScreenManager


class AppRomaneio(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type("on_theme_change")  # Cria o evento global

    def build(self):
        return MainScreenManager()

    def change_theme(self):
        """Função chamada pelos botões para alterar o tema."""
        self.theme_cls.theme_style = "Light" if self.theme_cls.theme_style == "Dark" else "Dark"
        self.dispatch("on_theme_change", self.theme_cls.theme_style)  # Dispara o evento global

    def on_theme_change(self, theme):
        """Evento chamado automaticamente quando o tema muda."""
        # print(f"[MainApp] Tema alterado para: {theme}")
            

if __name__ == "__main__":
    
    # config app...
    Window.size = (320, 600)

    AppRomaneio().run()