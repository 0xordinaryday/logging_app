from kivy.app import App
from kivy.lang import Builder
from kivymd.toast import toast
from kivymd.uix.list import OneLineListItem, ILeftBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.screen import MDScreen
from kivymd.uix.selectioncontrol import MDCheckbox

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
                text: "StrataT"
                # font_size: 10
                on_release: app.root.current = "strata"
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
                on_release: app.root.current = "new_project"
                
<ListItemWithCheckbox>:
    id: the_project
    markup: True

    LeftCheckbox:
        id: check
        on_release: 
            root.mark(check, the_project)

    IconRightWidget:
        icon: 'trash-can-outline'
        theme_text_color: "Custom"
        text_color: 1, 0, 0, 1
        on_release:
            root.delete_project(check, the_project)

''')


class HomeScreen(MDScreen):
    def on_enter(self, *args):
        # print('This prints automatically when App launches')
        """Event fired when the screen is displayed: the entering animation is
        complete."""
        try:
            project_details = db.get_project_information()
            self.ids.project_list.clear_widgets()  # if there are any already
            for project in project_details:
                self.ids.project_list.add_widget(
                    ListItemWithCheckbox(text=project[0] + ' ' + project[1], font_style='Body2',
                                         on_release=self.view_project))
        except Exception as e:
            print(e)
            pass

    def view_project(self, onelinelistitem):
        # print(onelinelistitem.text)
        App.get_running_app().root.current = "project_details"
        App.get_running_app().project_identifier = onelinelistitem.text.split(' ')[0]


class ListItemWithCheckbox(OneLineAvatarIconListItem):
    """Custom list item"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def mark(self, check, the_project):
        """mark the task as complete or incomplete"""
        if check.active:
            the_project.text = '[s]' + the_project.text + '[/s]'
        elif '[s]' in the_project.text:
            the_project.text = the_project.text[3:-4]
        else:
            pass

    def delete_project(self, check, the_project):
        """Delete the project"""
        if check.active:
            self.parent.remove_widget(the_project)
            print(the_project.text[3:].split(' ')[0])
            db.delete_project(the_project.text[3:].split(' ')[0])  # Here
        else:
            toast('Check the box if you want to delete the project')

class LeftCheckbox(ILeftBodyTouch, MDCheckbox):
    """Custom left container"""
