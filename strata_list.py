from kivy.app import App
from kivy.lang import Builder
from kivy.uix.togglebutton import ToggleButton
from kivymd.uix.list import OneLineListItem
from kivymd.uix.screen import MDScreen

from db import Database

# Initialize db instance
db = Database()

Builder.load_string('''
<StrataScreen>:
    id: strata_id
    name: "strata"
    
    MDBoxLayout:
        orientation: 'vertical'
        
        MDTopAppBar:
            id: topbar
            title: ''
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
                    id: interval_list
                    font_size: 10
            MDFloatingActionButton:
                icon: "plus"
                pos_hint: {"center_x": .85, "center_y": .15}
                on_release: app.root.current = "strata_details"

''')


class StrataScreen(MDScreen):

    def on_enter(self, *args):
        # print('This prints automatically when App launches')
        """Event fired when the screen is displayed: the entering animation is
        complete."""
        borehole_identifier = App.get_running_app().borehole_identifier
        self.ids.topbar.title = borehole_identifier + ' Intervals'
        try:
            # borehole_intervals = db.get_borehole_intervals(App.get_running_app().borehole_identifier)
            self.ids.interval_list.clear_widgets()  # if there are any already
            borehole_intervals = ['0.0 - 1.0', '1.0 - 1.5', '1.5 - 2.2', 'a', 'b', 'c', 'd', 'e', 'f']  # dummy list for now
            for interval in borehole_intervals:
                self.ids.interval_list.add_widget(OneLineListItem(text=interval, font_style='Body2'))
        except Exception as e:
            print(e)
            pass

    def add_interval(self):
        pass

        # borehole_to_create = ''
        #
        # current_borehole_id = App.get_running_app().borehole_identifier
        # current_job_id = App.get_running_app().project_identifier
        # highest_bh_name = db.get_highest_borehole_name(current_job_id)
        #
        # if not highest_bh_name:
        #     borehole_to_create = current_job_id + '-BH1'
        # else:
        #     borehole_to_create = current_job_id + '-BH' + str((int(highest_bh_name[0][0].split("BH", 1)[1])) + 1)
        #
        # App.get_running_app().borehole_identifier = borehole_to_create
        # App.get_running_app().root.current = "borehole_details"
