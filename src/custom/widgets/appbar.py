# developer BOY7 & Gustavo-Destroy

from kivy.metrics import dp

from kivymd.uix.boxlayout import MDBoxLayout

from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton

class CustomButtonIcon(MDIconButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pos_hint = {"center_y": 0.5}

class CustomTopAppBarTitle(MDLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.font_style = "Title"
        self.shorten = True
        self.shorten_from = "right"
        self.halign = "center"
        self.pos_hint = {"center_y": 0.45}

class CustomTopAppBarLeadingButtonContainer(MDBoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.adaptive_width=True

class CustomTopAppBarTrailingButtonContainer(MDBoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.adaptive_width=True

class CustomTopAppBar(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = None
        self.height = dp(64)

        self.padding = dp(4)
        self.spacing = dp(4)

        self.pos_hint = {'center_x': 0.5,'top': 1.0}

        # widgets internos
        self._leading_container = None
        self._title = None
        self._trailing_container = None

    def add_widget(self, widget):
        if isinstance(widget, CustomTopAppBarLeadingButtonContainer):
            if self._leading_container:
                self.remove_widget(self._leading_container)
            self._leading_container = widget

        elif isinstance(widget, CustomTopAppBarTitle):
            if self._title:
                self.remove_widget(self._title)
            self._title = widget

        elif isinstance(widget, CustomTopAppBarTrailingButtonContainer):
            if self._trailing_container:
                self.remove_widget(self._trailing_container)
            self._trailing_container = widget

        self.clear_widgets()

        if self._leading_container:
            super().add_widget(self._leading_container)

        if self._title:
            super().add_widget(self._title)

        if self._trailing_container:
            super().add_widget(self._trailing_container)