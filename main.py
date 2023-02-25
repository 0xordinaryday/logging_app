import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem
from kivy.properties import ObjectProperty

from homescreen import HomeScreen
from firstscreen import MyScreen1
from secondscreen import MyScreen2

from db import Database
# Initialize db instance
db = Database()



class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.material_style = "M3"
        sm = ScreenManager()
        sm.add_widget(HomeScreen())
        sm.add_widget(MyScreen1())
        sm.add_widget(MyScreen2())
        return sm


if __name__ == "__main__":
    MainApp().run()
