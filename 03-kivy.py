from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

Builder.load_file("kivy1.kv")

class ekran(GridLayout):
    pass

class uygulama(App):

    def build(self):
        return ekran()

if __name__ == "__main__":
    uygulama().run()


#kivy1.kv
"""
<ekran>:
    cols: 2

    Label:
        text: "User Name"
    TextInput:
        multiline: False
        password: False

    Label:
        text: "Password"
    TextInput:
        multiline: False
        password: True
"""