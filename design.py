from kivy.app import App 
from kivy.uix.button import Button 

class MyApp(App):
    def funcname(self):
        return Button(text='1')

MyApp().run()

