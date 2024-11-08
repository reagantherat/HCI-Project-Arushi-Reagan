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

#NAVIGATION
class MainWindow(Screen):
    def go_create_event(self):
        sm.current = "create_event"

class CreateEvent(Screen):
    def go_back(self):
        sm.current = "main"
    def month_popup(self):
        show_month_popup()
        ### TODO: set the value of the selection from the date to the actual value from the popup 
        # - will need to go to show_month_popup and get a returned value from there 
        # self.ids.month_select.text = value # (from show_month_popup)
        
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

#POPUPS
class MonthPopup(FloatLayout):
    pass
def show_month_popup():
    show = MonthPopup()

    monthPopup = Popup(title="Choose a month", content=show, size_hint=(None, None), size=(375, 500))
    monthPopup.open()
    ### TODO: return the date returned by the button

class DayPopup(FloatLayout):
    pass
def show_day_popup():
    show = DayPopup()

    dayPopup = Popup(title="Choose a day", content=show, size_hint=(None, None), size=(375, 500))
    dayPopup.open()
    ### TODO: see above

class YearPopup(FloatLayout):
    pass
def show_year_popup():
    show = YearPopup()

    yearPopup = Popup(title="Choose a year", content=show, size_hint=(None, None), size=(375, 500))
    yearPopup.open()
    ### TODO: see above

class MyMainApp(App):
    def build(self):
        return sm
        
if __name__ == "__main__":
    MyMainApp().run()