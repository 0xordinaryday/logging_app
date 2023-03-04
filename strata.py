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
            title: 'Strata'
            # size_hint: 1,0.1
            
        MDBoxLayout:
            # id: strata_box
            orientation: 'horizontal'
            spacing: "10dp"
            size_hint: 1,0.2
            ToggleButton:
                id: toggle_rock
                text: 'Rock' 
                group: 'material'
                on_release: root.talk_to_me(self)
            ToggleButton:
                id: toggle_soil
                text: 'Soil'
                group: 'material'
                on_release: root.talk_to_me(self)
                
        MDSeparator:
                
        MDBoxLayout:
            id: strata_box
            orientation: 'horizontal'
            spacing: "5dp"
            size_hint: 1,0.2
            
        MDSeparator:
            
        MDBoxLayout:
            id: prefix_box
            orientation: 'horizontal'
            spacing: "10dp"
            size_hint: 1.0,0.18
            
        MDSeparator:
                
        # MDBoxLayout:
        #     orientation: 'horizontal'
        #     spacing: "10dp"
        #     size_hint: 1,0.2
        #     ToggleButton:
        #         id: toggle_black
        #         text: 'Black' 
        #         group: 'colour'
        #         on_state: toggle_soil.state = "down" if toggle_soil.state == "normal" else "normal"
        #         on_release: root.talk_to_me(self)
        #     ToggleButton:
        #         id: toggle_white
        #         text: 'White'
        #         group: 'colour'
        #         state: 'down'
        #         on_release: root.talk_to_me(self)
            
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
                on_release: root.add_borehole()

''')


class StrataScreen(MDScreen):

    def removes_marks_all_chips(self, selected_instance_chip):
        for instance_chip in self.ids.chip_box.children:
            if instance_chip != selected_instance_chip:
                instance_chip.active = False

    def on_enter(self, *args):
        # print('This prints automatically when App launches')
        """Event fired when the screen is displayed: the entering animation is
        complete."""
        try:
            # borehole_intervals = db.get_borehole_intervals(App.get_running_app().borehole_identifier)
            self.ids.interval_list.clear_widgets()  # if there are any already
            borehole_intervals = ['0.0 - 1.0', '1.0 - 1.5', '1.5 - 2.2']
            for interval in borehole_intervals:
                self.ids.interval_list.add_widget(OneLineListItem(text=interval, font_style='Body2'))
        except Exception as e:
            print(e)
            pass

    def add_borehole(self):
        borehole_to_create = ''

        current_borehole_id = App.get_running_app().borehole_identifier
        current_job_id = App.get_running_app().project_identifier
        highest_bh_name = db.get_highest_borehole_name(current_job_id)

        if not highest_bh_name:
            borehole_to_create = current_job_id + '-BH1'
        else:
            borehole_to_create = current_job_id + '-BH' + str((int(highest_bh_name[0][0].split("BH", 1)[1])) + 1)

        App.get_running_app().borehole_identifier = borehole_to_create
        App.get_running_app().root.current = "borehole_details"

    def talk_to_me(self, instance):
        self.ids.strata_box.clear_widgets()
        self.ids.prefix_box.clear_widgets()
        if instance.text == 'Soil':
            stuff = ['CLAY', 'SILT', 'SAND', 'GRAVEL']
            for thing in stuff:
                toggle = ToggleButton(text=thing, group='major')
                self.ids.strata_box.add_widget(toggle)
            prefixes = ['Clayey', 'Silty', 'Sandy', 'Gravelly']
            for item in prefixes:
                toggle = ToggleButton(text=item)
                self.ids.prefix_box.add_widget(toggle)
            for child in self.ids.prefix_box.children:
                child.bind(on_release=self.child_selected)

    def child_selected(self, instance):
        for child in self.ids.prefix_box.children:
            if child.state == 'down':
                print(child.text, end=' ')
        for child in self.ids.strata_box.children:
            if child.state == 'down':
                print(child.text)
