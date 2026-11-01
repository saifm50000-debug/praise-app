from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
# red , green , blue , alfa
Window.clearcolor = (1,0,0,0)
Window.size = (400,600)
class NameApp(App):
    def build(self):
        self.title = "The Praise App (the first saif app)"
        layout = FloatLayout()

        self.texto = TextInput(
            text="your name",
            multiline = False,
            font_size=15,
            pos={147, 435},
            foreground_color=(0,0,0,1),
            size_hint=(None,None),
            size=(100, 45)
        )
        b1 = Button(text="press",
                   size_hint=(0.3,0.1),
                   pos_hint={"x":0.35,"y":0.60},
                   color=(1,1,1,1),
                   background_color=(0,0,1,1)
                   
                )
        self.l1 = Label(
            text="",
            font_size=32,
            color=(0,1,0,1),
            size_hint=(0.4,0.5),
            pos_hint={"x":0.3,"y":0.10}
        )
        layout.add_widget(self.texto)
        layout.add_widget(b1)
        layout.add_widget(self.l1)
        b1.bind(on_press=self.my_function)
        return layout
    
    def my_function(self, instance):
        if not self.config.has_section("Names"):
            self.config.add_section("Names")
        user_input = self.texto.text
        self.config.set("Names",user_input,"is the best")
        self.l1.text = f"{user_input} is the best"
        self.config.write()

if __name__=='__main__':
    NameApp().run()