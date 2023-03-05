from kivy.lang import Builder
from kivy.uix.togglebutton import ToggleButton
from kivymd.toast import toast
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
                 
                MDSeparator:   
                
                MDBoxLayout:
                    id: plasticity_or_grainsize_box
                    orientation: 'horizontal'
                    height: self.minimum_height
                    size_hint_y: '40dp'
                    spacing: "10dp"
                    # size_hint: 1.0,0.18


''')


class StrataDetailsScreen(MDScreen):
    QUALIFIER = ''
    PRIMARY_NAME = ''
    PRIMARY_CLASS = ''
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
    ALLOWABLE_PLASTICITY = {
        "CLAY": ["High Plast.", "Medium Plast.", "Low Plast."],
        "SILT": ["High Plast.", "Low Plast.", "Non-plastic"]
    }
    ALLOWABLE_GRAINSIZE = ["Fine", "Medium", "Coarse"]

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
                toggle.bind(on_release=self.strata_selected)

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
            self.ids.plasticity_or_grainsize_box.clear_widgets()
            for entry in prefixes:
                toggle = ToggleButton(text=entry, pos_hint={'x':1, 'y':-0.5})
                self.ids.prefix_box.add_widget(toggle)
                toggle.bind(on_release=self.prefix_selected)
            self.ids.working_name.text = self.PRIMARY_NAME
            if self.PRIMARY_NAME in ['CLAY', 'SILT']:
                self.PRIMARY_CLASS = 'FINE'
            else:
                self.PRIMARY_CLASS = 'COARSE'
        else:
            self.disable_children(self.ids.prefix_box)

    def prefix_selected(self, instance):
        self.PREFIX = ''  # set to empty string if previously selected

        for child in self.ids.prefix_box.children:
            if child.state == 'down':
                self.PREFIX = self.PREFIX + child.text + ' '

        if self.PRIMARY_CLASS == 'FINE':
            plasticity = self.ALLOWABLE_PLASTICITY[self.PRIMARY_NAME]
            self.ids.plasticity_or_grainsize_box.clear_widgets()
            group = None  # what a kludge
            if self.PRIMARY_NAME == 'SILT':
                group = 'silt'
            for entry in plasticity:
                toggle = ToggleButton(text=entry, pos_hint={'x': 1, 'y': -0.5}, group=group)
                self.ids.plasticity_or_grainsize_box.add_widget(toggle)
                toggle.bind(on_release=self.plasticity_selected)
        else:
            grainsize = self.ALLOWABLE_GRAINSIZE
            for entry in grainsize:
                toggle = ToggleButton(text=entry, pos_hint={'x': 1, 'y': -0.5})
                self.ids.plasticity_or_grainsize_box.add_widget(toggle)
                toggle.bind(on_release=self.grainsize_selected)

        self.ids.working_name.text = self.PREFIX + self.PRIMARY_NAME

    def plasticity_selected(self, instance):
        self.PRIMARY_PLASTICITY = ''
        high_selected = False
        med_selected = False
        low_selected = False
        non_selected = False

        for child in self.ids.plasticity_or_grainsize_box.children:
            if child.text == 'High Plast.' and child.state == 'down':
                high_selected = True
            if child.text == 'Medium Plast.' and child.state == 'down':
                med_selected = True
            if child.text == 'Low Plast.' and child.state == 'down':
                low_selected = True
            if child.text == 'Non-plastic' and child.state == 'down':
                non_selected = True

        if low_selected and high_selected:
            for child in self.ids.plasticity_or_grainsize_box.children:
                child.state = 'normal'
            toast("Can't be Low AND High")
            high_selected = False
            med_selected = False
            low_selected = False
            non_selected = False

        if low_selected and med_selected and not high_selected:
            self.PRIMARY_PLASTICITY = '; low to medium plasticity'
        if med_selected and high_selected and not low_selected:
            self.PRIMARY_PLASTICITY = '; medium to high plasticity'
        if low_selected and not med_selected and not high_selected:
            self.PRIMARY_PLASTICITY = '; low plasticity'
        if med_selected and not high_selected and not low_selected:
            self.PRIMARY_PLASTICITY = '; medium plasticity'
        if high_selected and not med_selected and not low_selected:
            self.PRIMARY_PLASTICITY = '; high plasticity'
        if non_selected:
            self.PRIMARY_PLASTICITY = '; non-plastic'

        self.ids.working_name.text = self.PREFIX + self.PRIMARY_NAME + self.PRIMARY_PLASTICITY

    def grainsize_selected(self, instance):
        self.PRIMARY_GRAINSIZE = ''
        coarse_selected = False
        med_selected = False
        fine_selected = False

        for child in self.ids.plasticity_or_grainsize_box.children:
            if child.text == 'Coarse' and child.state == 'down':
                coarse_selected = True
            if child.text == 'Medium' and child.state == 'down':
                med_selected = True
            if child.text == 'Fine' and child.state == 'down':
                fine_selected = True

        if fine_selected and not med_selected and not coarse_selected:
            self.PRIMARY_GRAINSIZE = '; fine grained'
        elif fine_selected and med_selected and not coarse_selected:
            self.PRIMARY_GRAINSIZE = '; fine to medium grained'
        elif fine_selected and med_selected and coarse_selected:
            self.PRIMARY_GRAINSIZE = '; fine to coarse grained'
        elif fine_selected and not med_selected and coarse_selected:
            self.PRIMARY_GRAINSIZE = '; fine and coarse grained (gap graded)'
        elif med_selected and not coarse_selected and not fine_selected:
            self.PRIMARY_GRAINSIZE = '; medium grained'
        elif med_selected and coarse_selected and not fine_selected:
            self.PRIMARY_GRAINSIZE = '; medium to coarse grained'
        elif coarse_selected and not med_selected and not fine_selected:
            self.PRIMARY_GRAINSIZE = '; coarse grained'
        else:
            self.PRIMARY_GRAINSIZE = ' undetermined grainsize'

        self.ids.working_name.text = self.PREFIX + self.PRIMARY_NAME + self.PRIMARY_GRAINSIZE

    def enable_children(self, widget):
        for child in widget.children:
            child.disabled = False

    def disable_children(self, widget):  # children are toggleboxes
        for child in widget.children:
            child.state = 'normal'  # i.e., unselected
            child.disabled = True
