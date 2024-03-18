from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

class giris(GridLayout):
  
  def __init__(self, **kwargs):
    super(giris,self).__init__(**kwargs)
    self.cols = 2

    self.kullaniciadi = Label(text = "User Name: ")
    self.add_widget(self.kullaniciadi)
    self.kullanici = TextInput(multiline = False)
    self.add_widget(self.kullanici)

    self.sifreyazi = Label(text = "Password: ")
    self.add_widget(self.sifreyazi)
    self.sifre = TextInput(multiline = False, password = true)
    self.add_widget(self.sifre)


class Uygulama(App):

 def build(self):
    return giris()
 
if __name__ == "__main__":
    Uygulama().run()
