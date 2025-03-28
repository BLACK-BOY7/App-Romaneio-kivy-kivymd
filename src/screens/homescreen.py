from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.uix.screen import MDScreen

from ..customeventdispatcher.themedwidget import ThemedWidget

from kivy.properties import (
    NumericProperty, StringProperty, AliasProperty, ReferenceListProperty,
    ObjectProperty, VariableListProperty, DictProperty, BooleanProperty)


Builder.load_file("src/screens_kv/homescreen.kv")


class HomeScreen(MDScreen,):
    _button_radius = VariableListProperty([dp(8), dp(8), dp(8), dp(8)])