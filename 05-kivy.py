from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.lang import Builder

Builder.load_file("kivy1.kv")

class yerlesim(GridLayout):
    pass

class uygulama(App):

    def build(self):
        return yerlesim()

if __name__ == "__main__":
    uygulama().run()


#kivy.kv
"""
<yerlesim>:
    cols:3
    padding:10
    spacing:5

    Button:
        text:"1"
        size_hint:2,1
    Button:
        text:"2"
        size_hint:1,1
    Button:
        text:"3"
        size_hint:1,1
    Button:
        text:"4"
        size_hint:1,1
    Button:
        text:"5"
        size_hint:1,1
    Button:
        text:"6"
        size_hint:1,1 
"""    