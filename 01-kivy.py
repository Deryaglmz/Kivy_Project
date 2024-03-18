from kivy.app import App
from kivy.uix.label import Label

class calisma(App):
    def build(self):
        return Label(text = "Merhaba Dünya")
    
if __name__ == "__main__":
    calisma().run()    