import kivy
from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup

# Set the window size
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '720')

# NAVIGATION
class MainWindow(Screen):
    def go_create_event(self):
        sm.current = "create_event"

class CreateEvent(Screen):
    def go_back(self):
        sm.current = "main"
    def month_clicked(self, val):
        print("month: " + val)
    def day_clicked(self, val):
        print("day: " + val)
    def year_clicked(self, val):
        print("year: " + val)
    def s_hour_clicked(self, val):
        print("s hour: " + val)
    def s_minute_clicked(self, val):
        print("s minute: " + val)
    def e_hour_clicked(self, val):
        print("e hour: " + val)
    def e_minute_clicked(self, val):
        print("e minute: " + val)
    def am_pm_clicked(self, instance, val, am_pm):
        if (val):
            print(am_pm)



class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")
sm = WindowManager()

screens = [MainWindow(name="main"), CreateEvent(name="create_event")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "main"

class MyMainApp(App):
    def build(self):
        return sm
        
if __name__ == "__main__":
    MyMainApp().run()