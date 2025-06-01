from __future__ import annotations

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.animation import Animation
from kivymd.uix.screen import MDScreen

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import MDList, MDListItem

from kivy.properties import (
    NumericProperty, StringProperty, AliasProperty, ReferenceListProperty,
    ObjectProperty, VariableListProperty, DictProperty, BooleanProperty)

# Custom Imports...
from ..database.controls import ControlClient, ControlOrder

Builder.load_file("src/screens_kv/romaneiosscreen.kv")

class RomaneiosScreen(MDScreen):
    _radius = VariableListProperty([dp(8), dp(8), dp(8), dp(8)])
    page: int = 0
    limit_page: int = 10

    def on_pre_enter(self):
        for i, order in enumerate(ControlOrder.get_orders_paginated(self.page, self.limit_page)):
            client = ControlClient.get_client_by_id(order.client_id)

            order_widget_info = RomaneioWidgetInfo(client_name=client.name,
                                                   wood_type=order.wood_type,
                                                    creatin_date=order.creatin_date)

            self.ids.romaneio_widgets.add_widget(order_widget_info)

    def on_pre_leave(self):
        child = self.ids.romaneio_widgets.children
        self.ids.romaneio_widgets.clear_widgets(child)

class RomaneiosWidgets(MDList):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ...
        

class RomaneioWidgetInfo(MDListItem):
    client_name: str = StringProperty("")
    wood_type: str = StringProperty("")
    creatin_date: str = StringProperty("")

class RomaneioWidgetFilter(MDBoxLayout):
    _radius = VariableListProperty([dp(4), dp(4), dp(4), dp(4)])