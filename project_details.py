from kivy import platform
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.toast import toast
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineListItem
from kivy.clock import Clock
from kivymd.uix.button import MDFloatingActionButton
from db import Database
from os.path import join
from excel_functions import chonkyboi
from androidstorage4kivy import SharedStorage, Chooser, ShareSheet
from android_permissions import AndroidPermissions

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
                        
            MDFloatingActionButton:
                icon: "send-outline"
                # md_bg_color: 'red'
                # icon_color: 'white' # app.theme_cls.primary_color
                pos_hint: {"center_x": .85, "center_y": .35}
                on_release: root.data_send(self)
                        
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
    test_uri = None

    def on_start(self):
        self.dont_gc = AndroidPermissions(self.start_app)
        self.test_uri = self.create_uri_for_sharesheet()

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
        someval = SharedStorage().copy_to_shared('logging_data.xlsx')
        toast('something')
        print('test')

    def data_send(self, b):
        file_to_share = self.create_uri_for_sharesheet()
        ShareSheet().share_file(file_to_share)
        self.button_reset(b)

    ### Callback ####

    def chooser_callback(self,uri_list):
        ShareSheet().share_file_list(uri_list, self.target)
        del self.chooser

    ### Utilities ####

    def button_reset(self, b):
        # The target app may timeout the button on_touch_up() event,
        # so the button fails to reset. Explicitly reset the button.
        Clock.schedule_once(b._do_release, b.min_state_time)

    def create_uri_for_sharesheet(self):
        filename = join(SharedStorage().get_cache_dir(), 'logging_data.xlsx')
        # create a file in Private storage
        shared_reference = SharedStorage().copy_to_shared(filename)  # returns reference to file, supposedly
        toast(shared_reference)
        return shared_reference
