from kivymd.app import MDApp

class ThemedWidget:
    """Mixin para adicionar suporte automático a mudanças de tema."""
    def __init__(self):
        app = MDApp.get_running_app()
        app.bind(on_theme_change=self.on_theme_update)

    def on_theme_update(self, app, theme):
        """Este método pode ser sobrescrito pelos widgets para personalizar a atualização do tema."""
        pass  # Padrão: não faz nada