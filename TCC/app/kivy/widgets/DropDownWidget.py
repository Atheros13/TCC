#-----------------------------------------------------------------------------#

### KIVY IMPORTS ###

from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown

#-----------------------------------------------------------------------------#

###

class DropDownWidget(Button):

    ''' '''

    def __init__(self, *args, text='', options=[], **kwargs):
        super(DropDownWidget, self).__init__(*args, **kwargs)

        self.dropdown = self.build_dropdown(options)
        self.dropdown.bind(on_select=lambda instance, x: setattr(self, 'text', x))

        self.bind(on_release=self.dropdown.open)

    def build_dropdown(self, options):

        dropdown = DropDown()

        for option in options:

            btn = Button(text=option, size_hint_y=None, height=20)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)

        return dropdown
