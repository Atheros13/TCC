#-----------------------------------------------------------------------------#

###

from kivy.uix.button import Button
from kivy.uix.label import Label 
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

#-----------------------------------------------------------------------------#

###

from app.kivy.widgets import DropDownWidget

#-----------------------------------------------------------------------------#

###

class LoginLayout(GridLayout):

    cols = 1
    padding = [10, 20, 20, 20]

    def __init__(self, *args, **kwargs):
        super(LoginLayout, self).__init__(*args, **kwargs)

        self.add_widget(self.build_login())

    def build_login(self):

        box = BoxLayout(orientation='horizontal', 
                        spacing=10,
                        size_hint_y=None, height=100)

        login = BoxLayout(orientation='vertical', size_hint_x=3, spacing=10)
        
        u = BoxLayout()
        self.username = DropDownWidget(size_hint_x=1.5, options=['Amanda', 'Alex', 'Adam', 'Michelle', 'Michael'])
        u.add_widget(Label(text='Name'))
        u.add_widget(self.username)

        p = BoxLayout()
        self.password = TextInput(size_hint_x=1.5)
        p.add_widget(Label(text='Password'))
        p.add_widget(self.password)

        login.add_widget(u)
        login.add_widget(p)
        box.add_widget(login)

        enter = Button(text='Login')
        enter.bind(on_release=self.login)
        box.add_widget(enter)

        return box

    def login(self, *args, **kwargs):

        print(self.username.text, self.password.text)
