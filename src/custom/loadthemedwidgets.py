from .themedwidgtes.modules import __modules__

class EventDispatcher:
    @staticmethod
    def on_update_theme():
        for module in __modules__:
            if hasattr(module, "on_update_theme"):
                module.on_update_theme()