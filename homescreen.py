from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineListItem
from kivy.clock import Clock
from kivymd.uix.button import MDFloatingActionButton
from db import Database

# Initialize db instance
db = Database()

Builder.load_string('''
<HomeScreen>:
    id: homescreen_id
    name: "homescreen"
    MDBoxLayout:
        orientation: 'vertical'
        
        MDTopAppBar:
            title: 'Projects'
            # size_hint: 1,0.1
            
        MDBoxLayout:
            spacing: "10dp"
            # adaptive_width: True
            size_hint: 0.9,0.3
            pos_hint: {"center_x": .5}
            MDFillRoundFlatButton:
                text: "Exit"
                # # font_size: 12
                md_bg_color: "#fefbff"
                on_release: app.stop()
                size_hint: 0.25, 0.3
                pos_hint: {"center_x": .5, "center_y": .5}
            MDFillRoundFlatButton:
                text: "Home"
                # # font_size: 12
                md_bg_color: "#fefbff"
                on_release: app.root.current = "homescreen"
                size_hint: 0.25, 0.3
                pos_hint: {"center_x": .5, "center_y": .5}
            MDFillRoundFlatButton:
                text: "Next"
                # font_size: 10
                on_release: app.root.current = "project_details"
                size_hint: 0.25, 0.3
                pos_hint: {"center_x": .5, "center_y": .5}
            
        MDFloatLayout:
            # size_hint: 1,0.6
            # pos_hint: {"top": 0.1}
            MDScrollView:
                MDList:
                    id: project_list
                    font_size: 10
            MDFloatingActionButton:
                icon: "plus"
                pos_hint: {"center_x": .85, "center_y": .15}
                

''')


class HomeScreen(MDScreen):
    def on_enter(self, *args):
        # print('This prints automatically when App launches')
        """Event fired when the screen is displayed: the entering animation is
        complete."""
        try:
            project_details = db.get_project_information()
            for project in project_details:
                self.ids.project_list.add_widget(OneLineListItem(text=project[0] + ' ' + project[1], font_style='Caption'))
        except Exception as e:
            print(e)
            pass

