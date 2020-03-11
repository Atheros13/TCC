#-----------------------------------------------------------------------------#

### KIVY IMPORTS ###

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder

#-----------------------------------------------------------------------------#

### APP IMPORTS ###

from app.main import MainClass

#-----------------------------------------------------------------------------#

### MAIN ###

class MainApp(App):

	title = 'TCC'

	def __init__(self, *args, **kwargs):
		super(MainApp, self).__init__(**kwargs)

		## Settings
		self.title = 'TCC'
		Window.size = (600, 400)

	def build(self):

		return MainClass().window

#-----------------------------------------------------------------------------#

### ENGINE ###

if __name__ == '__main__':

	MainApp().run()

#-----------------------------------------------------------------------------#

### CREATION ###

created_by = 'Atheros'

#-----------------------------------------------------------------------------#