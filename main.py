from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

from db import Database
from homescreen import HomeScreen
from new_project import NewProjectScreen
from project_details import ProjectDetailsScreen
from borehole_list import BoreholeListScreen
from borehole_details import BoreholeDetailsScreen
from strata_list import StrataScreen
from strata_details import StrataDetailsScreen

# Initialize db instance
db = Database()


class MainApp(MDApp):
    project_identifier = StringProperty('')  # blank to start with
    borehole_identifier = StringProperty('None set')  # blank to start with
    Window.softinput_mode = 'below_target'  # so keyboard doesn't cover textinput

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.material_style = "M3"
        sm = ScreenManager()
        sm.add_widget(HomeScreen())
        sm.add_widget(ProjectDetailsScreen())
        sm.add_widget(NewProjectScreen())
        sm.add_widget(BoreholeListScreen())
        sm.add_widget(BoreholeDetailsScreen())
        sm.add_widget(StrataScreen())
        sm.add_widget(StrataDetailsScreen())
        return sm


if __name__ == "__main__":
    MainApp().run()
