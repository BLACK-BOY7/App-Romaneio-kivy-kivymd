from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.uix.card import MDCard

from kivymd.uix.button import MDButton
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import MDList, MDListItem
from kivymd.uix.scrollview import MDScrollView


from kivy.properties import (
    NumericProperty, StringProperty, AliasProperty, ReferenceListProperty,
    ObjectProperty, VariableListProperty, DictProperty, BooleanProperty)


Builder.load_file("src/screens_kv/romaneiosscreen.kv")


class RomaneiosScreen(MDScreen):
    _radius = VariableListProperty([dp(8), dp(8), dp(8), dp(8)])

class RomaneiosWidgets(MDList):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for index in range(20):
            self.add_widget(RomaneioWidgetInfo())

class RomaneioWidgetInfo(MDListItem):
    ...

class RomaneioWidgetFilter(MDCard):
    _radius = VariableListProperty([dp(4), dp(4), dp(4), dp(4)])