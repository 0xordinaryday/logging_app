import datetime

from kivy.app import App
from kivy.lang import Builder
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen

from db import Database

# Initialize db instance
db = Database()

Builder.load_string('''
<BoreholeDetailsScreen>:
    id: borehole_details_id
    name: "borehole_details"
    
    MDBoxLayout:
        orientation: "vertical"
        
        MDTopAppBar:
            id: topbar
            title: 'Borehole Details'
            # size_hint: 1,0.1
            
        MDBoxLayout:
            spacing: "10dp"
            size_hint: 0.9,0.3
            pos_hint: {"center_x": .5}
            MDFillRoundFlatButton:
                text: "Intervals"
                # # font_size: 12
                md_bg_color: "#fefbff"
                on_release: app.root.current = "strata"
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
                do_scroll_x: False
                do_scroll_y: True    
                MDGridLayout:
                    cols: 1
                    size_hint_y: None
                    height: self.minimum_height
                    row_force_default: True
                    row_default_height: "40dp"
                    padding: 10
                        
                    MDLabel:
                        # md_bg_color: app.theme_cls.primary_light
                        font_size: '18sp'
                        bold: True
                        text: "Borehole ID"
                        
                    MDTextField:
                        id: borehole_id
                        font_size: '16sp'
                        text: ""
                        
                    MDLabel:
                        font_size: '18sp'
                        bold: True
                        text: "Easting"
                        # size_hint: 1,0.1
                        
                    MDTextField:
                        id: easting_id
                        font_size: '16sp'
                        text: ""
                        # size_hint: 1,0.1
                        
                    MDLabel:
                        font_size: '18sp'
                        bold: True
                        text: "Northing"
                        # size_hint: 1,0.1
                        
                    MDTextField:
                        id: northing_id
                        font_size: '16sp'
                        text: ""
                        # size_hint: 1,0.1
                        
                    MDLabel:
                        font_size: '18sp'
                        bold: True
                        text: "Elevation"
                        # size_hint: 1,0.1
                        
                    MDTextField:
                        id: elevation_id
                        font_size: '16sp'
                        text: ""
                        # size_hint: 1,0.1
                        
                    MDLabel:
                        font_size: '18sp'
                        bold: True
                        text: "Start Depth"
                        # size_hint: 1,0.1
                        
                    MDTextField:
                        id: startdepth_id
                        font_size: '16sp'
                        text: ""
                        # size_hint: 1,0.1
                            
                    MDLabel:
                        font_size: '18sp'
                        bold: True
                        text: "End Depth"
                        # size_hint: 1,0.1
                        
                    MDTextField:
                        id: enddepth_id
                        font_size: '16sp'
                        text: ""
                        # size_hint: 1,0.1 
                        
                    MDLabel:
                        font_size: '18sp'
                        bold: True
                        text: "Hole Dip"
                        # size_hint: 1,0.1
                        
                    MDTextField:
                        id: dip_id
                        font_size: '16sp'
                        text: ""
                        # size_hint: 1,0.1  
                            
                    MDLabel:
                        font_size: '18sp'
                        bold: True
                        text: "Hole Azimuth"
                        # size_hint: 1,0.1
                        
                    MDTextField:
                        id: azimuth_id
                        font_size: '16sp'
                        text: ""
                        # size_hint: 1,0.1         
                    
                    MDLabel:
                        font_size: '18sp'
                        bold: True
                        text: "Date Commenced"
                        # size_hint: 1,0.1
                        
                    MDTextField:
                        id: date_id
                        font_size: '16sp'
                        text: ""
                        # size_hint: 1,0.1
                        
                    MDLabel:
                        font_size: '18sp'
                        bold: True
                        text: "Logged By"
                        # size_hint: 1,0.1
                        
                    MDTextField:
                        id: logged_id
                        font_size: '16sp'
                        text: ""
                        # size_hint: 1,0.1
                        
                    MDLabel:
                        font_size: '18sp'
                        bold: True
                        text: "Rig"
                        # size_hint: 1,0.1
                        
                    MDTextField:
                        id: rig_id
                        font_size: '16sp'
                        text: ""
                        # size_hint: 1,0.1
                        
                    MDLabel:
                        font_size: '18sp'
                        bold: True
                        text: "Barrel Type"
                        # size_hint: 1,0.1
                        
                    MDTextField:
                        id: barrel_id
                        font_size: '16sp'
                        text: ""
                        # size_hint: 1,0.1
                        on_text: 
                            
                    MDLabel:
                        font_size: '18sp'
                        bold: True
                        text: "Fluid Used"
                        # size_hint: 1,0.1
                        
                    MDTextField:
                        id: fluid_id
                        font_size: '16sp'
                        text: ""
                        # size_hint: 1,0.1
                            
                    MDLabel:
                        font_size: '18sp'
                        bold: True
                        text: "Hole Diameter"
                        # size_hint: 1,0.1
                        
                    MDTextField:
                        id: diameter_id
                        font_size: '16sp'
                        text: ""
                        # size_hint: 1,0.1
            
            MDFloatingActionButton:
                icon: "delete"
                md_bg_color: 'red'
                icon_color: 'white' # app.theme_cls.primary_color
                pos_hint: {"center_x": .85, "center_y": .15}
                on_release: root.delete_borehole()            

''')


class BoreholeDetailsScreen(MDScreen):
    dialog = None

    def on_text(self, instance, value):
        db.update_collar_data(self.ids.borehole_id.text, float(self.ids.easting_id.text),
                              float(self.ids.northing_id.text), float(self.ids.elevation_id.text),
                              float(self.ids.startdepth_id.text), float(self.ids.enddepth_id.text),
                              int(self.ids.dip_id.text), int(self.ids.azimuth_id.text), self.ids.logged_id.text,
                              self.ids.date_id.text, self.ids.rig_id.text, self.ids.barrel_id.text,
                              self.ids.fluid_id.text, self.ids.diameter_id.text)

    def on_enter(self, *args):
        # print('This prints automatically when App launches')
        """Event fired when the screen is displayed: the entering animation is
        complete."""

        borehole_identifier = App.get_running_app().borehole_identifier
        self.ids.topbar.title = borehole_identifier + ' Details'
        try:
            # print(App.get_running_app().data) # a variable to hold the project number
            specific_borehole = db.get_specific_borehole_information(borehole_identifier)

            if not specific_borehole:  # does not yet exist
                self.ids.borehole_id.text = App.get_running_app().borehole_identifier
                self.ids.easting_id.text = '-1'
                self.ids.northing_id.text = '-1'
                self.ids.elevation_id.text = '-1'
                self.ids.startdepth_id.text = '0'
                self.ids.enddepth_id.text = '-1'
                self.ids.dip_id.text = '-90'
                self.ids.azimuth_id.text = '0'
                self.ids.logged_id.text = ''
                self.ids.date_id.text = datetime.date.today().strftime("%B %d, %Y")
                self.ids.rig_id.text = ''
                self.ids.barrel_id.text = ''
                self.ids.fluid_id.text = 'None'
                self.ids.diameter_id.text = ''
                db.create_borehole(self.ids.borehole_id.text, float(self.ids.easting_id.text),
                                   float(self.ids.northing_id.text), float(self.ids.elevation_id.text),
                                   float(self.ids.startdepth_id.text), float(self.ids.enddepth_id.text),
                                   int(self.ids.dip_id.text), int(self.ids.azimuth_id.text), self.ids.logged_id.text,
                                   self.ids.date_id.text, self.ids.rig_id.text, self.ids.barrel_id.text,
                                   self.ids.fluid_id.text, self.ids.diameter_id.text)
            else:
                bh = specific_borehole[0]
                self.ids.borehole_id.text = bh[0]
                self.ids.easting_id.text = str(bh[1])
                self.ids.northing_id.text = str(bh[2])
                self.ids.elevation_id.text = str(bh[3])
                self.ids.startdepth_id.text = str(bh[4])
                self.ids.enddepth_id.text = str(bh[5])
                self.ids.dip_id.text = str(bh[6])
                self.ids.azimuth_id.text = str(bh[7])
                self.ids.logged_id.text = bh[8]
                self.ids.date_id.text = bh[9]
                self.ids.rig_id.text = bh[10]
                self.ids.barrel_id.text = bh[11]
                self.ids.fluid_id.text = bh[12]
                self.ids.diameter_id.text = bh[13]

            self.ids.borehole_id.bind(text=self.on_text)
            self.ids.easting_id.bind(text=self.on_text)
            self.ids.northing_id.bind(text=self.on_text)
            self.ids.elevation_id.bind(text=self.on_text)
            self.ids.startdepth_id.bind(text=self.on_text)
            self.ids.enddepth_id.bind(text=self.on_text)
            self.ids.dip_id.bind(text=self.on_text)
            self.ids.azimuth_id.bind(text=self.on_text)
            self.ids.logged_id.bind(text=self.on_text)
            self.ids.date_id.bind(text=self.on_text)
            self.ids.rig_id.bind(text=self.on_text)
            self.ids.barrel_id.bind(text=self.on_text)
            self.ids.fluid_id.bind(text=self.on_text)
            self.ids.diameter_id.bind(text=self.on_text)

        except Exception as e:
            print(e)
            pass

    def delete_borehole(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Delete borehole?",
                text=App.get_running_app().borehole_identifier,
                buttons=[
                    MDFlatButton(
                        text="CANCEL", on_release=self.close_dialog
                    ),
                    MDRectangleFlatButton(
                        text="DELETE", on_release=self.delete_dialog
                    ),
                ],
            )

        self.dialog.open()

    def close_dialog(self, obj):
        # Close alert box
        self.dialog.dismiss()

    def delete_dialog(self, obj):
        # Close alert box
        self.dialog.dismiss()
        self.dialog = None
        db.delete_borehole(App.get_running_app().borehole_identifier)
        App.get_running_app().borehole_identifier = 'None set'
        App.get_running_app().root.current = "borehole_list"
