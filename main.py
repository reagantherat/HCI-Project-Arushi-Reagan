import kivy
from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.switch import Switch
from kivy.uix.checkbox import CheckBox 
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Rectangle, Color
from kivy.uix.recycleview import RecycleView

# Set the window size
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '720')

# NAVIGATION
class MainWindow(Screen):
    def go_create_event(self):
        sm.current = "create_event"
    def go_event_filters(self):
        sm.current = "event_filters"
    def go_message(self):
        sm.current = "message"
    def go_profile(self):
        sm.current = "profile"

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

class EventFilter(Screen):
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
    def switch_callback(self, switchObject, switchValue):
        if(switchValue):
            print('Switch is ON:):):)')
        else:
            print('Switch is OFF:(:(:(')
    def checkbox_click(self, instance, value):
        if value is True:
            print("Checkbox Checked")
        else:
            print("Checkbox Unchecked")

class Message(Screen):
    def go_back(self):
        sm.current = "main"

class WindowManager(ScreenManager):
    pass

class EventScroll(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        content = []
        my_file = open("eventdb.txt", "r")
        content_read = my_file.read()
        content = content_read.split("\n")
        my_file.close()
        for i in range(len(content)):
            content[i] = content[i].replace("|", "\n")
         
        self.data = [{'text': item} for item in content]

kv = Builder.load_file("my.kv")
sm = WindowManager()

screens = [MainWindow(name="main"), CreateEvent(name="create_event"), EventFilter(name="event_filters"), Message(name="message")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "main"

class MyMainApp(App):
    def build(self):
        return sm
        
if __name__ == "__main__":
    MyMainApp().run()