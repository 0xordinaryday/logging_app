from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

from db import Database
from firstscreen import MyScreen1
from homescreen import HomeScreen
from new_project import NewProjectScreen
from project_details import ProjectDetailsScreen
from secondscreen import MyScreen2
from borehole_list import BoreholeListScreen

# Initialize db instance
db = Database()


class MainApp(MDApp):
    data = StringProperty('some value')
    Window.softinput_mode = 'below_target'  # so keyboard doesn't cover textinput

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.material_style = "M3"
        sm = ScreenManager()
        sm.add_widget(HomeScreen())
        sm.add_widget(MyScreen1())
        sm.add_widget(MyScreen2())
        sm.add_widget(ProjectDetailsScreen())
        sm.add_widget(NewProjectScreen())
        sm.add_widget(BoreholeListScreen())
        return sm


if __name__ == "__main__":
    MainApp().run()
