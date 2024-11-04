import kivy
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
        def buil(self):
            return Label(text="This is a label")
        
if __name__ == "__main__":
      MyApp().run