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
    def month_handler(val):
        print(val)
        ### TODO: set the value of the selection from the date to the actual value from the popup 
        # - will need to go to show_month_popup and get a returned value from there 
        # self.ids.month_select.text = value # (from show_month_popup)
    def month_popup(self):
        show_month_popup()
    def day_popup(self):
        show_day_popup()
        ### TODO: see above
    def year_popup(self):
        show_year_popup()
        ### TODO: see above

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")
sm = WindowManager()

screens = [MainWindow(name="main"), CreateEvent(name="create_event")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "main"

# POPUPS
class MonthPopup(FloatLayout):
    def month_select(self, val):
        CreateEvent.month_handler(val)
    def close_popup(self):
        monthPopup.dismiss()
    
show = MonthPopup()
monthPopup = Popup(title="Choose a month", content=show, size_hint=(None, None), size=(375, 500))

def show_month_popup():
    monthPopup.open()


class DayPopup(FloatLayout):
    def day_select(self, val):
        print(val)
    def close_popup(self):
        dayPopup.dismiss()

show2 = DayPopup()
dayPopup = Popup(title="Choose a day", content=show2, size_hint=(None, None), size=(375, 500))

def show_day_popup():
    dayPopup.open()


class YearPopup(FloatLayout):
    def year_select(self, val):
        print(val)
    def close_popup(self):
        yearPopup.dismiss()

show3 = YearPopup()
yearPopup = Popup(title="Choose a year", content=show3, size_hint=(None, None), size=(375, 500))

def show_year_popup():
    yearPopup.open()

class MyMainApp(App):
    def build(self):
        return sm
        
if __name__ == "__main__":
    MyMainApp().run()