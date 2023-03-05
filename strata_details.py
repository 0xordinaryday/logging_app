from kivy.lang import Builder
from kivy.uix.togglebutton import ToggleButton
from kivymd.uix.screen import MDScreen

from db import Database

# Initialize db instance
db = Database()

Builder.load_string('''
<StrataDetailsScreen>:
    id: strata_details_id
    name: "strata_details"
    
    MDBoxLayout:
        orientation: 'vertical'
        
        MDTopAppBar:
            title: 'Interval Details'
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
            
        MDSeparator:
        
        MDLabel:
            id: working_name
            size_hint: 1, 0.15
            font_size: '14sp'
            # bold: True
            text: ''
            padding: [10,0]
            # pos_hint: {"x": 1, "y": -0.5}
        
        MDScrollView:
            do_scroll_x: False
            do_scroll_y: True    
            MDGridLayout:
                cols: 1
                size_hint_y: None
                height: self.minimum_height
                row_force_default: True
                row_default_height: "40dp"
                
                MDBoxLayout:
                    height: self.minimum_height
                    size_hint_y: '40dp'
                    id: depths
                    
                    MDLabel:
                        font_size: '16sp'
                        bold: True
                        text: 'From'
                        padding: [10,0]
                        pos_hint: {"x": 1, "y": -0.5}
                        
                    MDTextField:
                        id: depth_from_id
                        font_size: '16sp'
                        text: "0.0"
                        # size_hint: 1,0.1
                        on_text: 
                        padding: [10,0]
                        pos_hint: {"x": 1, "y": -0.5}
                        
                            
                    MDLabel:
                        font_size: '16sp'
                        bold: True
                        text: 'To'
                        padding: [10,0]
                        pos_hint: {"x": 1, "y": -0.5}
                        
                    MDTextField:
                        id: depth_to_id
                        font_size: '16sp'
                        text: "0.5"
                        padding: [10,0]
                        # size_hint: 1,0.1
                        on_text:
                        pos_hint: {"x": 1, "y": -0.5}
                    
                MDSeparator:    
                    
                MDBoxLayout:
                    # id: strata_box
                    orientation: 'horizontal'
                    spacing: "10dp"
                    height: self.minimum_height
                    size_hint_y: '40dp'
                    # size_hint: 1,0.2
                    ToggleButton:
                        id: toggle_rock
                        text: 'Rock' 
                        group: 'material'
                        on_release: root.insert_major(self)
                        pos_hint: {"x": 1, "y": -0.5}
                    ToggleButton:
                        id: toggle_soil
                        text: 'Soil'
                        group: 'material'
                        pos_hint: {"x": 1, "y": -0.5}
                        on_release: root.insert_major(self)
                        
                MDSeparator:
                        
                MDBoxLayout:
                    id: strata_box
                    orientation: 'horizontal'
                    spacing: "5dp"
                    height: self.minimum_height
                    # size_hint_y: '40dp'
                    size_hint: 1,0.2
                    
                MDSeparator:
                    
                MDBoxLayout:
                    id: prefix_box
                    orientation: 'horizontal'
                    height: self.minimum_height
                    size_hint_y: '40dp'
                    spacing: "10dp"
                    # size_hint: 1.0,0.18


''')


class StrataDetailsScreen(MDScreen):
    QUALIFIER = ''
    PRIMARY_NAME = ''
    PREFIX = ''
    PRIMARY_PLASTICITY = ''
    PRIMARY_GRAINSIZE = ''
    COLOUR = ''
    SECONDARY_NAME = ''
    SECONDARY_CHARS = ''
    ALLOWABLE_PREFIXES = {
        "CLAY": ["Silty", "Sandy", "Gravelly"],
        "SILT": ["Clayey", "Sandy", "Gravelly"],
        "SAND": ["Clayey", "Silty", "Gravelly"],
        "GRAVEL": ["Clayey", "Silty", "Sandy"]
    }

    def on_enter(self, *args):
        # print('This prints automatically when App launches')
        """Event fired when the screen is displayed: the entering animation is
        complete."""
        try:
            pass
        except Exception as e:
            print(e)
            pass

    def insert_major(self, instance):
        self.ids.strata_box.clear_widgets()
        self.ids.prefix_box.clear_widgets()
        if instance.text == 'Soil':
            primary_name = ['CLAY', 'SILT', 'SAND', 'GRAVEL']
            for entry in primary_name:
                toggle = ToggleButton(text=entry, group='major', pos_hint={'x':1, 'y':-0.5})
                self.ids.strata_box.add_widget(toggle)
            for child in self.ids.strata_box.children:
                child.bind(on_release=self.strata_selected)

    def strata_selected(self, instance):
        is_strata_selected = False

        for child in self.ids.strata_box.children:
            if child.state == 'down':
                is_strata_selected = True
                self.PRIMARY_NAME = child.text

        if is_strata_selected:
            self.enable_children(self.ids.prefix_box)
            prefixes = self.ALLOWABLE_PREFIXES[self.PRIMARY_NAME]
            self.ids.prefix_box.clear_widgets()
            for entry in prefixes:
                toggle = ToggleButton(text=entry, pos_hint={'x':1, 'y':-0.5})
                self.ids.prefix_box.add_widget(toggle)
                for child in self.ids.prefix_box.children:
                    child.bind(on_release=self.prefix_selected)
            self.ids.working_name.text = self.PRIMARY_NAME
        else:
            self.disable_children(self.ids.prefix_box)

    def prefix_selected(self, instance):
        self.PREFIX = ''  # set to empty string if previously selected

        for child in self.ids.prefix_box.children:
            if child.state == 'down':
                self.PREFIX = self.PREFIX + child.text + ' '

        self.ids.working_name.text = self.PREFIX + self.PRIMARY_NAME

    def enable_children(self, widget):
        for child in widget.children:
            child.disabled = False

    def disable_children(self, widget):  # children are toggleboxes
        for child in widget.children:
            child.state = 'normal'  # i.e., unselected
            child.disabled = True
