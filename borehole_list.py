from kivy.app import App
from kivy.lang import Builder
from kivymd.toast import toast
from kivymd.uix.list import OneLineListItem
from kivymd.uix.screen import MDScreen
from kivymd.uix.behaviors import TouchBehavior

from db import Database

# Initialize db instance
db = Database()

Builder.load_string('''
<BoreholeListScreen>:
    id: borehole_list_id
    name: "borehole_list"
    MDBoxLayout:
        orientation: 'vertical'
        
        MDTopAppBar:
            id: topbar
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
                    id: borehole_list
                    font_size: "14sp"
            MDFloatingActionButton:
                icon: "plus"
                pos_hint: {"center_x": .85, "center_y": .15}
                on_release: root.add_borehole()

''')


class BoreholeListScreen(MDScreen):
    def on_enter(self, *args):
        # print('This prints automatically when App launches')
        """Event fired when the screen is displayed: the entering animation is
        complete."""
        project_identifier = App.get_running_app().project_identifier
        self.ids.topbar.title = project_identifier + ' Boreholes'
        try:
            borehole_list = db.get_borehole_list(project_identifier)
            self.ids.borehole_list.clear_widgets()  # if there are any already
            for borehole in borehole_list:
                self.ids.borehole_list.add_widget(
                    OneLineListItem(text=borehole[0] + ' ' + borehole[3], font_style='Body2',
                                    on_release=self.view_borehole_details))
        except Exception as e:
            print(e)
            pass

    def view_borehole_details(self, onelinelistitem):
        App.get_running_app().borehole_identifier = onelinelistitem.text.split(' ')[0]
        App.get_running_app().root.current = "borehole_details"


    def add_borehole(self):

        current_borehole_id = App.get_running_app().borehole_identifier
        current_job_id = App.get_running_app().project_identifier
        highest_bh_name = db.get_highest_borehole_name(current_job_id)

        if not highest_bh_name:
            borehole_to_create = current_job_id + '-BH1'
        else:
            borehole_to_create = current_job_id + '-BH' + str((int(highest_bh_name[0][0].split("BH", 1)[1])) + 1)

        App.get_running_app().borehole_identifier = borehole_to_create
        App.get_running_app().root.current = "borehole_details"

