from kivy.app import App

class calisma(App):

    def build(self):
        pass

if __name__ == "__main__":
    calisma().run()


#calisma.kv
"""
FloatLayout

    pos_hint: {"center_x":0.5 , "center_y":0.5} 
    size_hint: 0.5,0.5
    canvas:
        Color:
            rgba: 0,1,0,1

        Rectangle:
            pos: self.pos
            size: self.size
"""        

### calisma 2
from kivy.app import App

class calisma(App):

    def build(self):
        pass

if __name__ == "__main__":
    calisma().run()


#calisma.kv
"""
FloatLayout

    pos_hint: {"center_x":0.5 , "center_y":0.5} 
    size_hint: 0.5,0.5
    canvas:
        Color:
            rgba: 0,1,0,1

        Ellipse:
            pos: self.pos
            size: self.size
"""    

### calisma 3
from kivy.app import App

class calisma(App):

    def build(self):
        pass

if __name__ == "__main__":
    calisma().run()


#calisma.kv
"""
FloatLayout

    pos_hint: {"center_x":0.5 , "center_y":0.5} 
    size_hint: 0.5,0.5
    canvas:
        Color:
            rgba: 0,1,0,1

        Line:
            points: 0,0,200,200,300,100
            width: 5
            close: True
            joint: "none"
"""   

### calisma 4
from kivy.app import App

class calisma(App):

    def build(self):
        pass

if __name__ == "__main__":
    calisma().run()


#calisma.kv
"""
FloatLayout
    pos_hint: {"center_x":0.5 , "center_y":0.5} 
    size_hint: 0.5,0.5

    canvas.before:
        Color:
            rgba: 0,1,0,1

        Rectangle:
            pos: self.pos
            size: self.size
    
    canvas:
        Color:
            rgba: 1,0,0,1

        Ellipse:
            pos: self.pos
            size: self.size
"""   

### calisma 5
from kivy.app import App

class calisma(App):

    def build(self):
        pass

if __name__ == "__main__":
    calisma().run()


#calisma.kv
"""
FloatLayout

    pos_hint: {"center_x":0.5 , "center_y":0.5} 
    size_hint: 0.5,0.5

    canvas:
        Color:
            rgba: 0,1,0,1

        Rectangle:
            pos: 100,100
            size: 100,100
    
    canvas.after:
        Color:
            rgba: 0,1,0,1

        Ellipse:
            pos: 400,400
            size: 100,100
    Scatter:
        Label:
            text: "KIVY"
"""       
