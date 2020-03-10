#-----------------------------------------------------------------------------#

###

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty, NumericProperty
from kivy.properties import ListProperty, DictProperty, BooleanProperty

from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label 
from kivy.uix.textinput import TextInput

from kivy.uix.gridlayout import GridLayout

#-----------------------------------------------------------------------------#

###

#-----------------------------------------------------------------------------#

###

class LoginLayout(GridLayout):

    cols=1
    padding = 20

    def __init__(self, *args, **kwargs):
        super(LoginLayout, self).__init__(*args, **kwargs)

        self.add_widget(self.build_login())

    def build_login(self):

        box = BoxLayout(orientation='horizontal')

        login = BoxLayout(orientation='vertical', size_hint_x=0.66, spacing=10)
        
        username = TextInput()
        password = TextInput()
        login.add_widget(username)
        login.add_widget(password)
        box.add_widget(login)

        enter = Button(text='Login')
        box.add_widget(enter)

        return box