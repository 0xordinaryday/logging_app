from kivy.app import App
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

from db import Database

# Initialize db instance
db = Database()

Builder.load_string('''
<NewProjectScreen>:
    id: new_project_id
    name: "new_project"
    
    MDBoxLayout:
        orientation: 'vertical'
        
        MDTopAppBar:
            title: 'New Project'
            # size_hint: 1,0.1
            
        MDLabel:
            font_size: '16sp'
            bold: True
            text: "Project Number"
            padding: (10,0)
            size_hint: 1,0.1
            
        MDTextField:
            padding: [10,0]
            id: project_number_id
            font_size: '14sp'
            hint_text: "Enter project number"
            size_hint: 1,0.1
            
        MDLabel:
            padding: (10,0)
            font_size: '16sp'
            bold: True
            text: "Project Type"
            size_hint: 1,0.1
            
        MDTextField:
            padding: (10,0)
            id: project_type_id
            font_size: '14sp'
            hint_text: "Enter project type"
            size_hint: 1,0.1
            
        MDLabel:
            padding: (10,0)
            font_size: '16sp'
            bold: True
            text: "Client"
            size_hint: 1,0.1
            
        MDTextField:
            padding: (10,0)
            id: client_id
            font_size: '14sp'
            hint_text: "Enter client"
            size_hint: 1,0.1
        
        MDLabel:
            font_size: '16sp'
            bold: True
            padding: (10,0)
            text: "Location"
            size_hint: 1,0.1
            
        MDTextField:
            padding: (10,0)
            id: location_id
            font_size: '14sp'
            hint_text: "Enter location"
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
                text: "Done"
                # font_size: 10
                on_release: root.commit_changes()
                size_hint: 0.25, 0.3
                pos_hint: {"center_x": .5, "center_y": .5}

''')


class NewProjectScreen(MDScreen):
    def on_enter(self, *args):
        # print('This prints automatically when App launches')
        """Event fired when the screen is displayed: the entering animation is
        complete."""
        try:
            pass
        except Exception as e:
            print(e)
            pass

    def commit_changes(self):
        db.create_project(self.ids.project_number_id.text, self.ids.client_id.text, self.ids.project_type_id.text,
                          self.ids.location_id.text)
        App.get_running_app().root.current = "homescreen"
