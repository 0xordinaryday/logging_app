from kivy.app import App
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
<ProjectDetailsScreen>:
    id: project_details_id
    name: "project_details"
    
    MDBoxLayout:
        orientation: 'vertical'
        
        MDTopAppBar:
            title: 'Project Details'
            # size_hint: 1,0.1
            
        MDLabel:
            font_size: '16sp'
            bold: True
            text: "Project Number"
            padding: (10,0)
            size_hint: 1,0.1
            
        MDLabel:
            padding: (10,0)
            id: project_number_id
            font_size: '14sp'
            text: ""
            size_hint: 1,0.1
            
        MDLabel:
            padding: (10,0)
            font_size: '16sp'
            bold: True
            text: "Project Type"
            size_hint: 1,0.1
            
        MDLabel:
            padding: (10,0)
            id: project_type_id
            font_size: '14sp'
            text: ""
            size_hint: 1,0.1
            
        MDLabel:
            padding: (10,0)
            font_size: '16sp'
            bold: True
            text: "Client"
            size_hint: 1,0.1
            
        MDLabel:
            padding: (10,0)
            id: client_id
            font_size: '14sp'
            text: ""
            size_hint: 1,0.1
        
        MDLabel:
            font_size: '16sp'
            bold: True
            padding: (10,0)
            text: "Location"
            size_hint: 1,0.1
            
        MDLabel:
            padding: (10,0)
            id: location_id
            font_size: '14sp'
            text: ""
            size_hint: 1,0.1
            
        MDBoxLayout:
            spacing: "10dp"
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
                text: "Boreholes"
                # font_size: 10
                on_release: app.root.current = "borehole_list"
                size_hint: 0.25, 0.3
                pos_hint: {"center_x": .5, "center_y": .5}

''')


class ProjectDetailsScreen(MDScreen):
    def on_enter(self, *args):
        # print('This prints automatically when App launches')
        """Event fired when the screen is displayed: the entering animation is
        complete."""
        try:
            # print(App.get_running_app().data) # a variable to hold the project number
            specific_project = db.get_specific_project_information(App.get_running_app().project_identifier)
            self.ids.project_number_id.text = specific_project[0]
            self.ids.client_id.text = specific_project[1]
            self.ids.location_id.text = specific_project[3]
            self.ids.project_type_id.text = specific_project[2]
            # specific_project[0] job_id
            # specific_project[1] client
            # specific_project[2] project_type
            # specific_project[3] location
        except Exception as e:
            print(e)
            pass

