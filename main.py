import kivy
from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.recycleview import RecycleView
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView

# Set the window size
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '720')

# NAVIGATION
class MainWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = []
        # Read database file content
        with open("eventdb.txt", "r") as my_file:
            content = my_file.read().split("\n")
        
        # Clean up the content
        for i in range(len(content)):
            content[i] = content[i].replace("|", "---", 1)
            content[i] = content[i].replace("|", "\n", 1)
            content[i] = content[i].replace("|", "---", 1)
            content[i] = content[i].replace("|", "\n")

        # Populate data for RecycleView with an on_release event to open the event screen
        self.data =  [{'text': item, 'on_release': lambda text=item: self.open_event_screen(text), "text_size": {self.width, None}, "halign": 'left', "valign": 'top'} for item in content]

    def go_create_event(self):
        sm.current = "create_event"
    def go_event_filters(self):
        sm.current = "event_filters"
    def go_message(self):
        sm.current = "message"
    def go_profile(self):
        sm.current = "profile"
    def open_event_screen(self, selected_item_text):
        # Get the event screen and set the selected item text
        event_screen = sm.get_screen("event")  # Ensure this points correctly to the screen manager
        event_screen.set_selected_item(selected_item_text)
        sm.current = "event"  # Switch to the event screen

    def refresh_event_scroll(self):
        self.ids.event_scroll.data = self.data
        self.ids.event_scroll.refresh_from_data()

    def populate_new_event(self, new_event):
        new_event = new_event.replace("|", "---", 1)
        new_event = new_event.replace("|", "\n", 1)
        new_event = new_event.replace("|", "---", 1)
        new_event = new_event.replace("|", "\n")

        self.data.append({'text': new_event, 'on_release': lambda text=new_event: self.open_event_screen(text), "text_size": {self.width, None}, "halign": 'left', "valign": 'top'})

class CreateEvent(Screen):
    def __init__(self,  **kwargs):
        super().__init__( **kwargs)
        self.data = [""] * 15
        self.cats = ""

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
        self.data[13] = self.cats
        self.data[14] = "1"

        self.allow_submit()

    def allow_submit(self):
        self.ids.error.text = ""
        for i in self.data:
            if i == "" or i == "Month" or i == "Day" or i == "Year":
                self.ids.error.text = "All fields are required"
        if self.ids.error.text == "":
            # write data to "database"
            f = open('eventdb.txt', 'a')
            to_add = "\n" + self.data[0] + " | " + self.data[1] +  " | " + self.data[3] + ":" + self.data[4] + " " + self.data[5] + " - " + self.data[6] + ":" + self.data[7] + " " + self.data[8] + " | " + self.data[9] + " " + self.data[10] + ", " + self.data[11] + " | " + self.data[2] + " | " + self.data[12] + " |" + self.data[13] + " | " + self.data[14]
            f.write(to_add)
            f.close()
            self.clear_inputs()

            #return to main page
            sm.get_screen("main").populate_new_event(to_add)
            sm.current = "main"
    
    def go_back(self):
        sm.current = "main"
    def s_am_pm_clicked(self, instance, val, am_pm):
        if (val):
            self.data[5] = am_pm
    def e_am_pm_clicked(self, instance, val, am_pm):
        if (val):
            self.data[8] = am_pm
    def category_clicked(self, instance, val, cat):
        if (val):
            self.cats = self.cats + cat
        else:
            self.cats = self.cats.replace(cat, '')
            
    def clear_inputs(self):
        self.ids.event_name.text = ""
        self.ids.event_organizer.text = ""
        self.ids.event_location.text = ""
        self.ids.s_hour_select.text = "00"
        self.ids.s_minute_select.text = "00"
        self.ids.e_hour_select.text = "00"
        self.ids.e_minute_select.text = "00"
        self.ids.month_select.text = "Month"
        self.ids.day_select.text = "Day"
        self.ids.year_select.text = "Year"
        self.ids.description.text = ""
        self.ids.s_am.active = False
        self.ids.s_pm.active = False
        self.ids.e_am.active = False
        self.ids.e_pm.active = False
        self.ids.cat_at.active = False
        self.ids.cat_sh.active = False
        self.ids.cat_wo.active = False
        self.ids.cat_so.active = False
        self.ids.cat_cl.active = False
        self.ids.cat_pr.active = False


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

    def reset_screen(self):
        # Reset message input field and the message list text
        self.ids.message_input.text = ""

        for widget in list(self.ids.layout.children):
            if isinstance(widget, Label):
                self.ids.layout.remove_widget(widget)

        self.show_go_together_button()

    def show_go_together_button(self):
        # Make sure the "Go Together" button is visible
        go_together_button = self.ids.go_together_button
        if go_together_button:
            go_together_button.opacity = 1  # Make button visible again
            go_together_button.disabled = False  # Enable button interaction

    def hide_go_together_button(self):
        go_together_button = self.ids.go_together_button
        if go_together_button:
            go_together_button.opacity = 0  # Make button invisible
            go_together_button.disabled = True  


class Profile(Screen):
    def go_back(self):
        sm.current = "main"

class Event(Screen):
    def go_back(self):
        self.manager.current = "main"
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.attendees_popup = None

    def set_selected_item(self, selected_item):
        # Update the label with the selected item's text
        self.ids.event_label.text = selected_item.replace("|", "\n")

    def open_attendees_popup(self):
        # Create and open the AttendeesPopup
        self.attendees_popup = AttendeesPopup()

        # Create the PeopleScroll instance
        people_scroll = PeopleScroll()

        layout = BoxLayout(orientation='vertical')

        button1 = Button(text="< Go back", size_hint_y=None, height=90, size_hint_x=None, width=200)
        button1.bind(on_release=self.close_popup)  # Bind the button to the 'add_to_list' method
        layout.add_widget(button1)

        # Bind the attendees_popup reference to the PeopleScroll instance
        people_scroll.attendees_popup = self.attendees_popup
        self.attendees_popup.people_scroll = people_scroll

        scroll_view = ScrollView()
        scroll_view.add_widget(people_scroll)

        layout.add_widget(scroll_view)

        button2 = Button(text="Can't find anyone? Add yourself to the list!", size_hint_y=None, height=90)
        button2.bind(on_release=self.add_to_list)  # Bind the button to the 'add_to_list' method
        layout.add_widget(button2)
        
        

        
        # Set the PeopleScroll as the content of the AttendeesPopup
        self.attendees_popup.content = layout

        # Open the popup
        self.attendees_popup.open()

    def add_to_list(self, instance):
        f = open('peopledb.txt', 'a')
        to_add = "\n" + "You have added yourself to this list!"
        f.write(to_add)
        f.close()

        if self.attendees_popup and self.attendees_popup.people_scroll:
            self.attendees_popup.people_scroll.populate_yourself(to_add)
        parent = instance.parent
        if parent:
            parent.remove_widget(instance)


    def close_popup(self, instance):
        if self.attendees_popup:
            self.attendees_popup.dismiss()  # Dismiss the popup
            self.attendees_popup = None

    
class WindowManager(ScreenManager):
    pass

class PeopleScroll(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.attendees_popup = None
        content = []
        my_file = open("peopledb.txt", "r")
        content_read = my_file.read()
        content = content_read.split("\n")
        my_file.close()
        for i in range(len(content)):
            content[i] = content[i].replace("|", "\n")
         
        self.data = [{'text': item, 'on_release': lambda text=item: self.open_message_screen(text)} for item in content]

    def populate_yourself(self, new_person):
        self.data.append({'text': new_person, 'on_release': lambda text=new_person: self.open_message_screen(text)})
        self.refresh_from_data()

    def open_message_screen(self, selected_item_text):
        # Call the go_message method from AttendeesPopup
        if self.attendees_popup:
            self.attendees_popup.go_message()
            

class AttendeesPopup(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def go_message(self):
        message_screen = sm.get_screen("message")
        message_screen.reset_screen()

        sm.current = "message"
        self.dismiss()


kv = Builder.load_file("my.kv")
sm = WindowManager()

screens = [MainWindow(name="main"), CreateEvent(name="create_event"), EventFilter(name="event_filters"), Message(name="message"), Profile(name="profile"), Event(name="event")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "main"

class MyMainApp(App):
    def build(self):
        return sm
        
    def remove_widget(self, widget):
        # Remove the button from its parent layout
        parent = widget.parent
        if parent:
            parent.remove_widget(widget)
        
if __name__ == "__main__":
    MyMainApp().run()