from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder

Builder.load_file("kivy1.kv")

class yerlesim(BoxLayout):
    pass

class uygulama(App):

    def build(self):
        return yerlesim()

if __name__ == "__main__":
    uygulama().run()


#kivy1.kv
"""
<yerlesim>:
    orientation:"horizontal" #vertical
    padding:10
    spacing:5

    Button:
        text:"1"
    Button:
        text:"2"
    Button:
        text:"3"
    Button:
        text:"4"
    Button:
        text:"5"
    Button:
        text:"6"  
"""    