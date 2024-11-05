import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.config import Config

from create_event import CreateEvent

# Set the window size
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '720')

class MyApp(App):
        def build(self):
            return CreateEvent()
        
if __name__ == "__main__":
      MyApp().run()