from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout

class video_player(RelativeLayout):

    def __init__(self, **kwargs):
        super(video_player, self).__init__(**kwargs)
        self.video.bind(position = self.slider)

    def slider(self,ins,val):
        self.ilerleme.value = float(val) / float(ins.duration)

    def oynat(self):
        self.video.state = "play"

    def duraklat(self):
        self.video.state = "pause"


    def durdur(self): 
        self.video.state = "stop" 

    def on_touch_down(self, touch):
        if self.ilerleme.collide_point(*touch.pos):
            self.video.unbind(position = self.slider)

        super(video_player,self).on_touch_down(touch)  

    def on_touch_up(self, touch):
        if self.ilerleme.collide_point(*touch.pos):
            self.video.bind(position = self.slider)  
            self.video.seek(self.ilerleme.value)  

class video(App):

    def build(self):
        return video_player()
    
if __name__ == "__main__":
    video().run()    


#video.kv
"""
<video_player>:

    video: _video
    ilerleme: _ilerleme

    Video:
        id: _video
        source : "linustorvalds.mp4"
        play: true  

    BoxLayout:
        size_hint:1,0.05
        orientation: "horizontal"

        Button:
            size: 33,33
            size_hint:None, None
            background_normal:"play_1.png"
            background_ndown:"play_2.png"
            on_press: root.oynat()

        Button:
            size: 33,33
            size_hint:None, None
            background_normal:"pause_1.png"
            background_ndown:"pause_2.png"
            on_press: root.duraklat()

        Button:
            size: 33,33
            size_hint:None, None
            background_normal:"stop_1.png"
            background_ndown:"stop_2.png"   
            on_press: root.durdur()   

        Slider:
        id: _ilerleme
        max: 1
        min: 0
        value: 0
        pos_hint: {"center_x":0.5 ,"center_y":0.5 }
        size_hint: 1,None
"""