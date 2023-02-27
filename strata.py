from kivy.animation import Animation
from kivy.app import App
from kivy.lang import Builder
from kivymd.toast import toast
from kivymd.uix.chip import MDChip
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
        id: chip_box
        adaptive_size: True
        spacing: "8dp"

        MyChip:
            text: "ROCK"
            on_active: if self.active: root.removes_marks_all_chips(self)

        MyChip:
            text: "SOIL"
            active: True
            on_active: if self.active: root.removes_marks_all_chips(self)
                
    MDBoxLayout:
        orientation: 'vertical'
        
        MDTopAppBar:
            title: 'Strata'
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
            borehole_list = db.get_borehole_list(App.get_running_app().project_identifier)
            self.ids.borehole_list.clear_widgets()  # if there are any already
            for borehole in borehole_list:
                self.ids.borehole_list.add_widget(
                    OneLineListItem(text=borehole[0] + ' ' + borehole[3], font_style='Body2',
                                    on_release=self.view_borehole_details))
        except Exception as e:
            print(e)
            pass

    def view_borehole_details(self, onelinelistitem):
        # print(onelinelistitem.text)
        App.get_running_app().borehole_identifier = onelinelistitem.text.split(' ')[0]
        App.get_running_app().root.current = "borehole_details"


    def add_borehole(self):
        borehole_to_create = ''

        current_borehole_id = App.get_running_app().borehole_identifier
        current_job_id = App.get_running_app().project_identifier
        highest_bh_name = db.get_highest_borehole_name(current_job_id)
        # print(highest_bh_name[0][0])
        # print(current_borehole_id)
        # print(current_job_id)

        if not highest_bh_name:
            borehole_to_create = current_job_id + '-BH1'
        else:
            borehole_to_create = current_job_id + '-BH' + str((int(highest_bh_name[0][0].split("BH", 1)[1])) + 1)

        App.get_running_app().borehole_identifier = borehole_to_create
        App.get_running_app().root.current = "borehole_details"

class MyChip(MDChip):
    icon_check_color = (0, 0, 0, 1)
    text_color = (0, 0, 0, 0.5)
    _no_ripple_effect = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(active=self.set_chip_bg_color)
        self.bind(active=self.set_chip_text_color)

    def set_chip_bg_color(self, instance_chip, active_value: int):
        '''
        Will be called every time the chip is activated/deactivated.
        Sets the background color of the chip.
        '''

        self.md_bg_color = (
            (0, 0, 0, 0.4)
            if active_value
            else (
                self.theme_cls.bg_darkest
                if self.theme_cls.theme_style == "Light"
                else (
                    self.theme_cls.bg_light
                    if not self.disabled
                    else self.theme_cls.disabled_hint_text_color
                )
            )
        )

    def set_chip_text_color(self, instance_chip, active_value: int):
        Animation(
            color=(0, 0, 0, 1) if active_value else (0, 0, 0, 0.5), d=0.2
        ).start(self.ids.label)