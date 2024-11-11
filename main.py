import kivy
from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
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
    def __init__(self,  **kwargs):
        super().__init__( **kwargs)
        self.data = [""] * 15
        self.data[3] = '0'
        self.data[4] = '0'
        self.data[6] = '0'
        self.data[7] = '0'
        self.data[14] = '1'

    # Name | Organizer | Location | Start Hour : Start Minute AM/PM - End Hour : End Minute AM/PM | Month Day, Year | Description | Tags | Num People
    def on_submit(self):
        self.data[0] = (self.ids.event_name.text)
        self.data[1] = (self.ids.event_organizer.text)
        self.data[2] = (self.ids.event_location.text)
        self.data[3] = (self.ids.s_hour_select.text)
        self.data[4] = (self.ids.s_minute_select.text)
        self.data[6] = (self.ids.e_hour_select.text)
        self.data[7] = (self.ids.e_minute_select.text)
        self.data[9] = (self.ids.month_select.text)
        self.data[10] = (self.ids.day_select.text)
        self.data[11] = (self.ids.year_select.text)
        self.data[12] = (self.ids.description.text)
        self.data[13] = ""
        self.data[14] = "1"

        print(self.data)

        # write data to "database"
        f = open('eventdb.txt', 'a')
        to_add = "\n" + self.data[0] + " | " + self.data[1] + " | " + self.data[2] + " | " + self.data[3] + ":" + self.data[4] + " " + self.data[5] + " - " + self.data[6] + ":" + self.data[7] + " " + self.data[8] + " | " + self.data[9] + " " + self.data[10] + ", " + self.data[11] + " | " + self.data[12] + " | " + self.data[13] + " | " + self.data[14]
        print(to_add)
        f.write(to_add)
        f.close()

        #return to main page
        sm.current = "main"
   
    def go_back(self):
        sm.current = "main"
    def s_am_pm_clicked(self, instance, val, am_pm):
        if (val):
            self.data[5] = am_pm
    def e_am_pm_clicked(self, instance, val, am_pm):
        if (val):
            self.data[8] = am_pm
            print(self.data)     

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

    def __init__(self, **kwargs):
        super(Message, self).__init__(**kwargs)

    def addthelabel(self):
        # Retrieve text from the TextInput
        text = self.ids.message_input.text.strip()  # Gets and removes extra spaces

        # Only add a label if there is text entered
        if text:
            # Create a new label with the text from the TextInput
            new_label = Label(text=text, size_hint_y=None, height="40dp")
            
            # Add the label to the layout inside the ScrollView
            self.ids.layout.add_widget(new_label)

            # Clear the TextInput field after adding the label
            self.ids.message_input.text = ""
            
            # Scroll to the bottom of the ScrollView to show the latest message
            self.ids.scroll_view.scroll_to(new_label)

class Profile(Screen):
    def go_back(self):
        sm.current = "main"

class Event(Screen):
    def go_back(self):
        self.manager.current = "main"
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def set_selected_item(self, selected_item):
        # Update the label with the selected item's text
        self.ids.event_label.text = selected_item.replace("|", "\n")
    
class WindowManager(ScreenManager):
    pass

class EventScroll(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Read file content
        with open("eventdb.txt", "r") as my_file:
            content = my_file.read().split("\n")
        
        # Clean up the content
        for i in range(len(content)):
            content[i] = content[i].replace("|", "\n")
        
        # Populate data for RecycleView with an on_release event to open the event screen
        self.data = [{'text': item, 'on_release': lambda text=item: self.open_event_screen(text), "text_size": {self.width, None}, "halign": 'left', "valign": 'top'} for item in content]

    def open_event_screen(self, selected_item_text):
        # Get the event screen and set the selected item text
        event_screen = self.parent.parent.manager.get_screen("event")  # Ensure this points correctly to the screen manager
        event_screen.set_selected_item(selected_item_text)
        self.parent.parent.manager.current = "event"  # Switch to the event screen

class PeopleScroll(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        content = []
        my_file = open("peopledb.txt", "r")
        content_read = my_file.read()
        content = content_read.split("\n")
        my_file.close()
        for i in range(len(content)):
            content[i] = content[i].replace("|", "\n")
         
        self.data = [{'text': item} for item in content]


kv = Builder.load_file("my.kv")
sm = WindowManager()

screens = [MainWindow(name="main"), CreateEvent(name="create_event"), EventFilter(name="event_filters"), Message(name="message"), Profile(name="profile"), Event(name="event")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "main"

class MyMainApp(App):
    def build(self):
        return sm
        
if __name__ == "__main__":
    MyMainApp().run()