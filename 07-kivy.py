from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

class resim(GridLayout):
    pass

class uygulama(App):

    def build(self):
        return resim()

if __name__ == "__main__":
    Window.clearcolor = (0.5,0.5,0.5,1)
    uygulama().run()


#uygulama.kv
"""
<resim>:
    cols: 2

    Image:
        source: "resim.jpg"
    Image:
        source: "resim2.png"
    Image:
        source: "resim3.png"
    Image:
        source: "resim4.webp"
"""    