from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color

class cizim(Widget):

    def on_touch_down(self, touch):
        with self.canvas:
            Color(0,0,1)

            touch.ud["Line"] = Line(points = (touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud["Line"].points += (touch.x, touch.y)

class fare(App):

    def build(self):
        return cizim()

if __name__ == "__main__":
    fare().run()