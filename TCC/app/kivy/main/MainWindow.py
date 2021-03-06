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

### KV-LANG ###

Builder.load_string('''

<MainWindow>:
	
	canvas.before:
		Color:
			rgba: 1, 1, 1, 1
		Rectangle:
			size: self.size
			pos: self.pos	
	spacing: 5	
	
	GridLayout:
		cols: 1
		padding: 1
		spacing: 1
		canvas.before:
			Color:
				rgba: 0, 0, 0, 1
			Rectangle:
				size: self.size
				pos: self.pos		
		size_hint_x: 0.2
		id: sidebody
		
		ScrollView:
			size_hint_y: None
			id: scroll
			GridLayout:
				cols: 1
				size_hint_y: None
				height: 0
				id: sidebar

	GridLayout:
		cols: 1
		canvas.before:
			Color:
				rgba: 0, 0, 0, 1
			Rectangle:
				size: self.size
				pos: self.pos	
		id: body		

''')

#-----------------------------------------------------------------------------#

class MainWindow(BoxLayout):

    orientation = 'horizontal'

    def add_page(self, page):

        for child in self.ids.body.children:
            self.ids.body.remove_widget(child)

        self.ids.body.add_widget(page)
