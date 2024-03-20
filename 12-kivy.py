from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Line, Color , Rectangle, Ellipse
from kivy.uix.button import Button

class yerlesim(FloatLayout):
    pass

class secim(BoxLayout):
    
    def renk_kirmizi(self):
        global renk
        renk ="kirmizi"

    def renk_yesil(self):
        global renk
        renk ="yesil"

    def renk_mavi(self):
        global renk
        renk ="mavi" 

    def sekil_kare(self):
        global sekil
        sekil ="kare" 

    def sekil_elips(self):
        global sekil
        sekil ="elips"

    def sekil_cizgi(self):
        global sekil
        sekil ="cizgi"                    

class cizim(BoxLayout):

    global renk
    global sekil

    renk = "beyaz"
    sekil = "cizgi"

    def on_touch_down(self, touch):
        with self.canvas:
            if renk == "kirmizi":
                Color(1,0,0)
            elif renk == "yesil":
                Color(0,1,0) 
            elif renk == "mavi":
                Color(0,0,1)  
            else:
                Color(1,1,1) 

            if sekil == "cizgi":
                touch.ud["Line"] = Line(points = (touch.x, touch.y))
            elif sekil == "kare":
                touch.ud["kare"] = Rectangle(pos = (touch.x, touch.y) , size = (10,10))
            elif sekil == "elips":
                touch.ud["elips"] = Ellipse(pos = (touch.x, touch.y) , size = (10,10)) 

    def on_touch_move(self, touch):

        if sekil == "cizgi":
            touch.ud["Line"].points += (touch.x, touch.y)
        elif sekil == "kare":
            touch.ud["kare"].pos = (touch.x, touch.y)
        elif sekil == "elips":
            touch.ud["elips"].pos = (touch.x, touch.y)


class paint(App):

    def build(self):

        self.buton = Button(text=  ("temizle"))
        self.buton.bind(on_press = self.temizle)

        self.yerlesim = yerlesim()

        self.secim = secim()
        self.cizim = cizim()

        self.secim.add_widget(self.buton)
        self.yerlesim.add_widget(self.cizim) 
        self.yerlesim.add_widget(self.secim)  

        return self.yerlesim
    
    def temizle(self, obj):
        self.cizim.canvas.clear()

if __name__ == "__main__":
    paint().run()


#paint.kv
"""
<secim>

    orientation: "vertical"
    size_hint: 0.2,1

    Button:
        text: "kare"
        on_press: root.sekil_kare()
    Button:
        text: "elips"
        on_press: root.sekil_elips()
    Button:
        text: "cizgi"
        on_press: root.sekil_cizgi()
    Button:
        text: "kirmizi"
        on_press: root.renk_kirmizi()
    Button:
        text: "yesil" 
        on_press: root.renk_yesil()
    Button:
        text: "mavi" 
        on_press: root.renk_mavi()   
"""
