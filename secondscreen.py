from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.screen import MDScreen


class MyScreen2(MDScreen):
    pass


Builder.load_string('''
<MyScreen2>:
    name: "secondscreen"
    Label:
        text: 'Second Screen'
    MDFillRoundFlatButton:
        text: "Home"
        md_bg_color: "#fefbff"
        # font_size: 12
        on_release: app.root.current = "homescreen"
        size: 75, 50
        size_hint: None, None
        pos_hint: {"center_x": .5, "center_y": .1}
    MDFillRoundFlatButton:
        text: "First Screen"
        # font_size: 10
        on_release: app.root.current = "firstscreen"
        size: 75, 50
        size_hint: None, None
        pos_hint: {"center_x": .9, "center_y": .1}
''')
