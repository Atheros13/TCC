#-----------------------------------------------------------------------------#

### KIVY IMPORTS ###

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.graphics.vertex_instructions import Line
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty, NumericProperty
from kivy.properties import ListProperty, DictProperty, BooleanProperty

from kivy.uix.button import Button
from kivy.uix.carousel import Carousel
from kivy.uix.checkbox import CheckBox
from kivy.uix.colorpicker import ColorPicker, ColorWheel
from kivy.uix.dropdown import DropDown
from kivy.uix.filechooser import FileChooserIconView, FileChooserListView
from kivy.uix.image import Image, AsyncImage
from kivy.uix.label import Label 
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem



#-----------------------------------------------------------------------------#

### PYTHON IMPORTS ###

import os
import os.path
import platform
import sqlite3
import smtplib
import subprocess
import time

#-----------------------------------------------------------------------------#

### MAIN APP ###

class MainApp(App):

	title = 'TCC'

	def __init__(self, *args, **kwargs):
		super(MainApp, self).__init__(**kwargs)

		## Settings
		self.title = 'TCC'

	def build(self):
		
		return BoxLayout()

#-----------------------------------------------------------------------------#

### ENGINE ###

if __name__ == '__main__':

	MainApp().run()

#-----------------------------------------------------------------------------#

### CREATION ###

created_by = 'Atheros'

#-----------------------------------------------------------------------------#