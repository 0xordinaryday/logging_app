try:
    from androidstorage4kivy import SharedStorage
except:
    ImportError
from kivy.app import App
from kivy.lang import Builder
from kivymd.toast import toast
from kivymd.uix.screen import MDScreen

from android_permissions import AndroidPermissions
from db import Database
from excel_functions import chonkyboi

# Initialize db instance
db = Database()

Builder.load_string('''
<ProjectDetailsScreen>:
    id: project_details_id
    name: "project_details"
    
    MDBoxLayout:
        orientation: 'vertical'
        
        MDTopAppBar:
            id: topbar
            title: 'Project Details'
            # size_hint: 1,0.1
            
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
        
        MDFloatLayout:
            MDScrollView:
                MDGridLayout:
                    cols: 1
                    size_hint_y: None
                    height: self.minimum_height
                    row_force_default: True
                    row_default_height: "40dp"
                    padding: 10
                
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
                        
            #MDFloatingActionButton:
            #    icon: "send-outline"
            #    # md_bg_color: 'red'
            #    # icon_color: 'white' # app.theme_cls.primary_color
            #    pos_hint: {"center_x": .85, "center_y": .35}
            #    on_release: root.data_send(self)
                        
            MDFloatingActionButton:
                icon: "database-export-outline"
                # md_bg_color: 'red'
                # icon_color: 'white' # app.theme_cls.primary_color
                pos_hint: {"center_x": .85, "center_y": .15}
                on_release: root.data_export()
            
''')


class ProjectDetailsScreen(MDScreen):
    private_files = None
    dont_gc = None

    def on_start(self):
        self.dont_gc = AndroidPermissions(self.start_app)

    def on_enter(self, *args):
        # print('This prints automatically when App launches')
        """Event fired when the screen is displayed: the entering animation is
        complete."""
        project_identifier = App.get_running_app().project_identifier
        self.ids.topbar.title = project_identifier + ' Details'
        try:
            specific_project = db.get_specific_project_information(project_identifier)
            self.ids.project_number_id.text = specific_project[0]
            self.ids.client_id.text = specific_project[1]
            self.ids.location_id.text = specific_project[3]
            self.ids.project_type_id.text = specific_project[2]
        except Exception as e:
            print(e)
            pass

    def data_export(self):
        chonkyboi()
        SharedStorage().copy_to_shared('logging_data.xlsx')
        toast('Data saved')
