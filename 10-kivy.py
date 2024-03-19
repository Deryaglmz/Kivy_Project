from kivy.app import App
from kivy.uix.widget import Widget

class cizim(Widget):

    def on_touch_down(self, touch):
        print(touch)

    def on_touch_move(self, touch):
        print(touch)

    def on_touch_up(self, touch):
        print(touch)

class fare(App):

    def build(self):
        return cizim()

if __name__ == "__main__":
    fare().run()
