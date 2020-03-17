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
from kivy.uix.stacklayout import StackLayout
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

### APP IMPORTS ###

from app.database import Database

from app.kivy.layouts import LoginLayout
from app.kivy.main import MainWindow

from app.models.staff import Staff

#-----------------------------------------------------------------------------#

class MainClass():

	def __init__(self, *args, **kwargs):

		self.window = MainWindow()

		## Build
		self.db = Database('tcc')
		self.staff = self.build_staff()

		self.login_layout = self.build_login_layout()

		## Engine
		self.window.add_page(self.login_layout)

	##

	def build_staff(self):

		staff_data = self.db.cursor.execute('''SELECT * from staff
											ORDER BY firstname ASC''').fetchall()
		staff_list = []
		for staff in staff_data:
			s = Staff(staff)

			if s.name == 'Michael Atheros':
				staff_list = [s] + staff_list
			else:
				staff_list.append(s)

		return staff_list

	def build_login_layout(self):

		return LoginLayout(login=self.login, staff=self.staff)

	def login(self, *args, **kwargs):

		staff = self.login_layout.username.text