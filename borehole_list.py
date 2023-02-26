from kivy.app import App
from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem
from kivymd.uix.screen import MDScreen

from db import Database

# Initialize db instance
db = Database()

Builder.load_string('''
<HomeScreen>:
    id: borehole_list_id
    name: "borehole_list"
    MDBoxLayout:
        orientation: 'vertical'
        
        MDTopAppBar:
            title: 'Project Boreholes'
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


class BoreholeList(MDScreen):
    def on_enter(self, *args):
        # print('This prints automatically when App launches')
        """Event fired when the screen is displayed: the entering animation is
        complete."""
        try:
            project_details = db.get_project_information()
            self.ids.project_list.clear_widgets()  # if there are any already
            for project in project_details:
                self.ids.project_list.add_widget(
                    OneLineListItem(text=project[0] + ' ' + project[1], font_style='Body2',
                                    on_release=self.do_something))
        except Exception as e:
            print(e)
            pass

    def do_something(self, onelinelistitem):
        # print(onelinelistitem.text)
        App.get_running_app().root.current = "project_details"
        App.get_running_app().data = onelinelistitem.text.split(' ')[0]
