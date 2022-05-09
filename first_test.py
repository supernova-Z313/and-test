from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class SayHello(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1

        self.window.add_widget(Image(source="hehe.png"))
        self.first_text = Label(text="ARA ARA !!")
        self.window.add_widget(self.first_text)
        self.first_in = TextInput(multiline=False)
        self.window.add_widget(self.first_in)
        self.innn = Button(text="enterrrrr")
        self.window.add_widget(self.innn)
        self.innn.bind(on_press=self.colb)
        return self.window

    def colb(self, ass):
        self.first_text.text = "fuck the" + self.first_in.text

if __name__ == "__main__":
    SayHello().run()
