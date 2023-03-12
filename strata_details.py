from functools import partial

from kivy.lang import Builder
from kivy.properties import ColorProperty
from kivy.uix.togglebutton import ToggleButton
from kivymd.toast import toast
from kivymd.uix.list import ILeftBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.screen import MDScreen
from kivymd.uix.selectioncontrol import MDCheckbox

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
            MDBoxLayout:
                height: self.minimum_height
                orientation: 'vertical'
                size_hint_y: None
                
                MDBoxLayout:
                    height: self.minimum_height
                    size_hint_y: None
                    id: depths
                    
                    MDLabel:
                        font_size: '16sp'
                        bold: True
                        text: 'From'
                        padding: [10,0]
                        # pos_hint: {"x": 1, "y": -0.5}
                        
                    MDTextField:
                        id: depth_from_id
                        font_size: '16sp'
                        text: "0.0"
                        # size_hint: 1,0.1
                        on_text: 
                        padding: [10,0]
                        # pos_hint: {"x": 1, "y": -0.5}
                            
                    MDLabel:
                        font_size: '16sp'
                        bold: True
                        text: 'To'
                        padding: [10,0]
                        # pos_hint: {"x": 1, "y": -0.5}
                        
                    MDTextField:
                        id: depth_to_id
                        font_size: '16sp'
                        text: "0.5"
                        padding: [10,0]
                        # size_hint: 1,0.1
                        on_text:
                        # pos_hint: {"x": 1, "y": -0.5}
                   
                MDBoxLayout:
                    # id: strata_box
                    orientation: 'horizontal'
                    spacing: "10dp"
                    height: "40dp"
                    size_hint_y: None
                    # size_hint: 1,0.2
                    ToggleButton:
                        id: toggle_rock
                        text: 'Rock' 
                        group: 'material'
                        on_release: root.insert_major(self)
                        # pos_hint: {"x": 1, "y": -0.5}
                    ToggleButton:
                        id: toggle_soil
                        text: 'Soil'
                        group: 'material'
                        # pos_hint: {"x": 1, "y": -0.5}
                        on_release: root.insert_major(self)
                      
                MDBoxLayout:
                    id: strata_box
                    orientation: 'horizontal'
                    spacing: "10dp"
                    height: "40dp"
                    size_hint_y: None
                    # size_hint: 1,0.2
                    
                MDBoxLayout:
                    orientation: 'horizontal'
                    height: "15dp"
                    size_hint_y: None

                MDBoxLayout:
                    id: plasticity_or_grainsize_box
                    orientation: 'horizontal'
                    height: self.minimum_height
                    size_hint_y: None
                    spacing: "10dp"
                    height: "40dp"
                    # size_hint: 1.0,0.18
                    
                MDBoxLayout:
                    orientation: 'horizontal'
                    height: "15dp"
                    size_hint_y: None

                MDList:
                    id: colour_list
                    font_size: "14sp"
 
                MDBoxLayout:
                    # spacer
                    orientation: 'horizontal'
                    height: self.minimum_height
                    size_hint_y: None
                    height: "10dp"
                    
                MDBoxLayout:
                    orientation: 'horizontal'
                    height: "15dp"
                    size_hint_y: None
                    
                MDBoxLayout:
                    # label
                    height: self.minimum_height
                    size_hint_y: None
                    id: secondary_components
                    
                    MDLabel:
                        font_size: '16sp'
                        bold: True
                        id: first_secondary_label
                        text: 'First Secondary Component'
                        padding: [10,0]

                MDBoxLayout:
                    # buttons here
                    id: first_secondary
                    orientation: 'horizontal'
                    height: self.minimum_height
                    size_hint_y: None
                    spacing: "10dp"
                    height: "40dp"
                    # size_hint: 1.0,0.18
                    
                MDBoxLayout:
                    #spacer
                    orientation: 'horizontal'
                    height: "35dp"
                    size_hint_y: None
                    
                MDBoxLayout:
                    # label
                    height: self.minimum_height
                    size_hint_y: None
                    id: secondary_components
                    
                    MDLabel:
                        font_size: '16sp'
                        bold: True
                        id: second_secondary_label
                        text: 'Second Secondary Component'
                        padding: [10,0]

                MDBoxLayout:
                    id: second_secondary
                    orientation: 'horizontal'
                    height: self.minimum_height
                    size_hint_y: None
                    spacing: "10dp"
                    height: "40dp"
                    # size_hint: 1.0,0.18
                    
                MDBoxLayout:
                    orientation: 'horizontal'
                    height: "15dp"
                    size_hint_y: None

                MDBoxLayout:
                    id: secondary_grainsize_box
                    orientation: 'horizontal'
                    # height: self.minimum_height
                    size_hint_y: None
                    spacing: "10dp"
                    height: "40dp"
                    # size_hint: 1.0,0.18
                    
                MDBoxLayout:
                    #spacer
                    orientation: 'horizontal'
                    height: "35dp"
                    size_hint_y: None
                    
                MDBoxLayout:
                    # label
                    height: self.minimum_height
                    size_hint_y: None
                    
                    MDLabel:
                        font_size: '16sp'
                        bold: True
                        id: third_secondary_label
                        text: 'Third Secondary Component'
                        padding: [10,0]

                MDBoxLayout:
                    id: third_secondary
                    orientation: 'horizontal'
                    height: self.minimum_height
                    size_hint_y: None
                    spacing: "10dp"
                    height: "40dp"
                    # size_hint: 1.0,0.18
                    
                MDBoxLayout:
                    #spacer
                    orientation: 'horizontal'
                    height: "35dp"
                    size_hint_y: None
                    
                MDBoxLayout:
                    id: terminal_spacer
                    orientation: 'horizontal'
                    height: self.minimum_height
                    size_hint_y: None
                    height: "40dp"
                    
<ColourItemWithCheckbox>:
    id: colour_listitem
    markup: True
    custom_icon_colour: self.custom_icon_colour

    LeftCheckbox:
        id: check
        on_release: root.parent.parent.parent.parent.parent.mark(check, colour_listitem)

    IconRightWidget:
        icon: 'square-rounded' 
        theme_text_color: "Custom"
        text_color: root.custom_icon_colour
        icon_size: "40dp"

''')


def get_prefix_text(instance):
    if instance.group == 'sand_fraction':
        prefix_text = 'Sandy'
    elif instance.group == 'gravel_fraction':
        prefix_text = 'Gravelly'
    elif 'Silt' in instance.text:
        prefix_text = 'Silty'
    elif 'Clay' in instance.text:
        prefix_text = 'Clayey'
    else:
        prefix_text = instance.text
    return prefix_text


class StrataDetailsScreen(MDScreen):
    QUALIFIER = ''
    PRIMARY_NAME = ''
    PRIMARY_CLASS = ''
    PREFIX = []
    PRIMARY_PLASTICITY = ''
    PRIMARY_GRAINSIZE = ''
    COLOURS = []
    COLOUR_STRING = ''
    SECONDARY_NAME = ''
    SECONDARY_CHARACTERISTICS = ''
    TERTIARY_NAME = ''
    TERTIARY_CHARACTERISTICS = ''
    ALLOWABLE_SOILS = ["CLAY", "SILT", "SAND", "GRAVEL"]
    ALLOWABLE_PLASTICITY = {
        "CLAY": ["High Plast.", "Medium Plast.", "Low Plast."],
        "SILT": ["High Plast.", "Low Plast.", "Non-plastic"]
    }
    ALLOWABLE_GRAINSIZE = ["Fine", "Medium", "Coarse"]
    ALLOWABLE_COLOURS = {
        "Brown": "peru",
        "Dark Brown": "saddlebrown",
        "Red": "firebrick",
        "Red-brown": "maroon",
        "Orange": "darkorange",
        "Orange-brown": "sandybrown",
        "Yellow": "khaki",
        "Yellow-brown": "goldenrod",
        "Grey": "lightslategrey",
        "Dark Grey": "dimgrey",
        "Black": "black",
        "White": "ivory",
        "Green": "darkolivegreen",
        "Blue": "darkslateblue"
    }
    ALLOWABLE_SECONDARY_PROPORTIONS = {
        "COARSE": ["Nil", "≤15%", ">15, ≤30%", ">30%"],
        "FINE": ["Nil", "≤5%", ">5, ≤12%", ">12%"]
    }
    secondaries_are_set = False
    accessory_grainsize_set = False

    # ALLOWABLE_COLOUR_ACTIONS = ["Done", "Reset", "and", "mottled"]
    # ALLOWABLE_COLOUR_MODIFIERS = ["Very Dark", "Dark", "Light"]

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
        if instance.text == 'Soil':
            primary_name = ['CLAY', 'SILT', 'SAND', 'GRAVEL']
            for entry in primary_name:
                toggle = ToggleButton(text=entry, group='major', pos_hint={'x': 1, 'y': -0.5})
                self.ids.strata_box.add_widget(toggle)
                toggle.bind(on_release=self.strata_selected)

    def strata_selected(self, instance):
        is_strata_selected = False
        self.reset_secondaries()
        self.ids.plasticity_or_grainsize_box.clear_widgets()
        self.COLOUR_STRING = ''
        self.COLOURS = []

        for child in self.ids.strata_box.children:
            if child.state == 'down':
                is_strata_selected = True
                self.PRIMARY_NAME = child.text

        if is_strata_selected:
            self.ids.working_name.text = self.PRIMARY_NAME
            if self.PRIMARY_NAME in ['CLAY', 'SILT']:
                self.PRIMARY_CLASS = 'FINE'
            else:
                self.PRIMARY_CLASS = 'COARSE'
            self.setup_plasticity_or_grainsize()
            self.set_secondaries()

    def setup_plasticity_or_grainsize(self):
        if self.PRIMARY_CLASS == 'FINE':
            plasticity = self.ALLOWABLE_PLASTICITY[self.PRIMARY_NAME]
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
                toggle_callback = partial(self.grainsize_selected, level='Primary')
                toggle.bind(on_release=toggle_callback)

        self.update_name()
        self.populate_colours()

    def plasticity_selected(self, instance):
        self.PRIMARY_PLASTICITY = ''
        self.PRIMARY_GRAINSIZE = ''
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

        self.update_name()

    def grainsize_selected(self, instance, level):
        children_ids = ''

        if level == 'Primary':
            self.PRIMARY_GRAINSIZE = ''
            self.PRIMARY_PLASTICITY = ''
            children_ids = self.ids.plasticity_or_grainsize_box.children
        else:
            children_ids = ''
        coarse_selected = False
        med_selected = False
        fine_selected = False

        for child in children_ids:
            if child.text == 'Coarse' and child.state == 'down':
                coarse_selected = True
            if child.text == 'Medium' and child.state == 'down':
                med_selected = True
            if child.text == 'Fine' and child.state == 'down':
                fine_selected = True

        if fine_selected and not med_selected and not coarse_selected:
            output_text = '; fine grained'
        elif fine_selected and med_selected and not coarse_selected:
            output_text = '; fine to medium grained'
        elif fine_selected and med_selected and coarse_selected:
            output_text = '; fine to coarse grained'
        elif fine_selected and not med_selected and coarse_selected:
            output_text = '; fine and coarse grained (gap graded)'
        elif med_selected and not coarse_selected and not fine_selected:
            output_text = '; medium grained'
        elif med_selected and coarse_selected and not fine_selected:
            output_text = '; medium to coarse grained'
        elif coarse_selected and not med_selected and not fine_selected:
            output_text = '; coarse grained'
        else:
            output_text = ' undetermined grainsize'

        if level == 'Primary':
            self.PRIMARY_GRAINSIZE = output_text

        self.update_name()

    def populate_colours(self, *args):
        colours = self.ALLOWABLE_COLOURS
        self.ids.colour_list.clear_widgets()

        for colour in [*colours]:
            listitem = ColourItemWithCheckbox(text=colour, font_style='Body2', custom_icon_colour=colours[colour])
            self.ids.colour_list.add_widget(listitem)

    def mark(self, check, instance):
        if check.active:
            self.COLOURS.append(instance.text.lower())
        else:
            self.COLOURS.remove(instance.text.lower())
        self.display_colours()

    def display_colours(self):
        if not len(self.COLOURS):
            self.COLOUR_STRING = ''
        elif (len(self.COLOURS)) == 1:
            self.COLOUR_STRING = '; ' + self.COLOURS[0]
        elif (len(self.COLOURS)) == 2 and self.PRIMARY_NAME == 'CLAY':
            self.COLOUR_STRING = '; ' + self.COLOURS[0] + ' mottled ' + self.COLOURS[1]
        elif (len(self.COLOURS)) > 2 and self.PRIMARY_NAME == 'CLAY':
            self.COLOUR_STRING = '; ' + self.COLOURS[0] + ' mottled ' + '{} and {}'.format(
                ', '.join(self.COLOURS[1:-1]), self.COLOURS[-1])
        else:
            self.COLOUR_STRING = '; ' + '{} and {}'.format(', '.join(self.COLOURS[:-1]), self.COLOURS[-1])

        self.update_name()

    def set_secondaries(self):
        if self.PRIMARY_CLASS == 'FINE':
            self.ids.second_secondary_label.text = 'Sand'
            self.ids.third_secondary_label.text = 'Gravel'
            self.set_coarse_secondaries()

            if self.PRIMARY_NAME == 'CLAY':
                self.ids.first_secondary_label.text = 'Silt'
                secondary_prefix = ['Silty', 'Not Silty']
            else:
                self.ids.first_secondary_label.text = 'Clay'
                secondary_prefix = ['Clayey', 'Not Clayey']
            # print(secondary_prefix)
            for entry in secondary_prefix:
                toggle = ToggleButton(text=entry, pos_hint={'x': 1, 'y': -0.5}, group='secondary_group')
                self.ids.first_secondary.add_widget(toggle)
                toggle_callback = partial(self.handle_fine_prefix)
                toggle.bind(on_release=toggle_callback)

        self.secondaries_are_set = True

    def set_coarse_secondaries(self):
        coarse = self.ALLOWABLE_SECONDARY_PROPORTIONS['COARSE']
        for entry in coarse:
            toggle_sand = ToggleButton(text=entry, pos_hint={'x': 1, 'y': -0.5}, group='sand_fraction')
            toggle_gravel = ToggleButton(text=entry, pos_hint={'x': 1, 'y': -0.5}, group='gravel_fraction')
            self.ids.second_secondary.add_widget(toggle_sand)
            self.ids.third_secondary.add_widget(toggle_gravel)
            toggle_sand.bind(on_release=self.set_second_secondary_fraction)
            toggle_gravel.bind(on_release=self.set_second_secondary_fraction)

    def set_second_secondary_fraction(self, instance):
        # "Nil", "≤15%", ">15, ≤30%", ">30%"
        if instance.text != 'Nil' and not self.accessory_grainsize_set:
            grainsize = self.ALLOWABLE_GRAINSIZE
            self.accessory_grainsize_set = True
            for entry in grainsize:
                toggle = ToggleButton(text=entry, pos_hint={'x': 1, 'y': -0.5})
                self.ids.secondary_grainsize_box.add_widget(toggle)
                toggle_callback = partial(self.grainsize_selected, level='Secondary')
                toggle.bind(on_release=toggle_callback)

        if instance.text != '>30%' and instance.state == 'down':
            self.remove_prefix(instance)
        if instance.text == '>30%' and instance.state == 'normal':
            self.remove_prefix(instance)
        if instance.text == '≤15%':
            pass
            # print(instance.group)
        elif instance.text == '>15, ≤30%':
            pass
        elif instance.text == '>30%' and instance.state == 'down':
            self.add_prefix(instance)

    def set_third_secondary_fraction(self, instance):
        pass

    def remove_prefix(self, instance):
        prefix_text_to_remove = get_prefix_text(instance)
        if len(self.PREFIX) == 1 and prefix_text_to_remove in self.PREFIX:
            self.PREFIX = []
        elif prefix_text_to_remove in self.PREFIX:
            self.PREFIX.remove(prefix_text_to_remove)

        self.update_name()

    def add_prefix(self, instance):
        prefix_text_to_add = get_prefix_text(instance)
        if prefix_text_to_add not in self.PREFIX:
            self.PREFIX.append(prefix_text_to_add)

        self.update_name()

    def update_name(self):
        prefix_text = ' '.join(self.PREFIX) + ' '
        self.ids.working_name.text = prefix_text + self.PRIMARY_NAME + self.PRIMARY_PLASTICITY + \
                                     self.PRIMARY_GRAINSIZE + self.COLOUR_STRING + self.SECONDARY_NAME + \
                                     self.SECONDARY_CHARACTERISTICS + self.TERTIARY_NAME + \
                                     self.TERTIARY_CHARACTERISTICS

    def reset_secondaries(self):
        self.ids.first_secondary_label.text = 'First Accessory'
        self.ids.second_secondary_label.text = 'Second Accessory'
        self.ids.third_secondary_label.text = 'Third Accessory'
        self.ids.first_secondary.clear_widgets()
        self.ids.second_secondary.clear_widgets()
        self.ids.third_secondary.clear_widgets()

    def enable_children(self, widget):
        for child in widget.children:
            child.disabled = False

    def disable_children(self, widget):  # children are toggleboxes
        for child in widget.children:
            child.state = 'normal'  # i.e., unselected
            child.disabled = True

    def handle_fine_prefix(self, instance):
        if 'Not' not in instance.text and instance.state == 'down':
            self.add_prefix(instance)
        elif 'Not' in instance.text and instance.state == 'down':
            self.remove_prefix(instance)
        elif 'Not' not in instance.text and instance.state == 'normal':
            self.remove_prefix(instance)

class ColourItemWithCheckbox(OneLineAvatarIconListItem):
    """Custom list item"""
    custom_icon_colour = ColorProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def mark(self, check, instance):
        pass


class LeftCheckbox(ILeftBodyTouch, MDCheckbox):
    """Custom left container"""
