from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.screen import MDScreen


class MyScreen1(MDScreen):
    pass


Builder.load_string('''
<MyScreen1>:
    name: "firstscreen"
    Label:
        text: 'First Screen'
    MDFillRoundFlatButton:
        text: "Home"
        # font_size: 12
        d_bg_color: "#fefbff"
        on_release: app.root.current = "homescreen"
        size: 75, 50
        size_hint: None, None
        pos_hint: {"center_x": .5, "center_y": .1}
    MDFillRoundFlatButton:
        text: "Second Screen"
        # font_size: 10
        on_release: app.root.current = "secondscreen"
        size: 75, 50
        size_hint: None, None
        pos_hint: {"center_x": .1, "center_y": .1}
''')
