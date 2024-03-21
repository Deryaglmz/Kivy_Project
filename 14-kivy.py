from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.config import Config

Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '400')

class CalculatorApp(App):
    def build(self):
        self.expression = ""
        self.result_label = Label(text="0", font_size=40, size_hint_y=None, height=80)
        layout = GridLayout(cols=4, spacing=5)
        
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        
        for button in buttons:
            if button == '=':
                btn = Button(text=button, font_size=40)
                btn.bind(on_press=self.calculate)
            elif button == 'C':
                btn = Button(text=button, font_size=40)
                btn.bind(on_press=self.clear)
            else:
                btn = Button(text=button, font_size=40)
                btn.bind(on_press=self.append)
            layout.add_widget(btn)
        layout.add_widget(self.result_label)
        
        return layout
    
    def append(self, instance):
        self.expression += instance.text
        self.result_label.text = self.expression
    
    def clear(self, instance):
        self.expression = ""
        self.result_label.text = "0"
    
    def calculate(self, instance):
        try:
            self.expression = str(eval(self.expression))
            self.result_label.text = self.expression
        except:
            self.result_label.text = "Error"

if __name__ == "__main__":
    CalculatorApp().run()
