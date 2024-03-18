from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class uygulama(App):

    def build(self):
        pass

if __name__ == "__main__":
    uygulama().run()



#uygulama.kv
"""
FloatLayout

    Button:
        text: "Merhaba Kivy"
        size_hint: 0.4,0.2
        pos_hint: {"x":0 , "y":0.5} 

    Button:
        text: "Merhaba Kivy"
        size_hint: 0.2,0.2
        pos_hint: {"right":0.3 , "top":0.5} 
"""    