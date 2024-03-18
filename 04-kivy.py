from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.lang import Builder

Builder.load_file("kivy1.kv")

class etiket(Widget):
    pass

class uygulama(App):

    def build(self):
        return etiket()

if __name__ == "__main__":
    uygulama().run()


#kivy1.kv
"""
<etiket>:
    Button:
        text:"Click Here"
        pos:0, 0
        size:100, 100 # Sol alt
        # pos: root.x, root.top - self.height (sol üst köşe)
        # pos: root.center_x - self.width / 2, root.center_y - self.height / 2 (ortada)  
        # pos: root.right - self.width,0 (sağ alt köşe) 
        # pos: 70 , 80
""" 