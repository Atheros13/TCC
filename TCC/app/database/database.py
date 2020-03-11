#-----------------------------------------------------------------------------#





#-----------------------------------------------------------------------------#

### PYTHON IMPORTS ###

import os
import os.path
import sqlite3
import subprocess

#-----------------------------------------------------------------------------#

### CLASS ###

class Database():
	
	'''
	Use to access connection and cursor for creating/updating/deleting data,
	also has built in methods which allow for quick request of stored data
	'''

	def __init__(self, file, *args, **kwargs):

		self.file = file
		filename = os.path.join(os.path.abspath("."), '%s.db' % self.file)
		
		try:
			self.connection = sqlite3.connect(filename) # allows for TIMESTAMP
	
		except Exception:

			base_path = sys._MEIPASS # exists in temp dif
			tempfilename = os.path.join(base_path, '%s.db' % self.file)

			connection = sqlite3.connect(tempfilename) # access temp file
			copyfile(tempfilename, filename) # copy temp file to path
			connection.close() # close temp file
			self.connection = sqlite3.connect(filename) # open path file

		self.cursor = self.connection.cursor()

	def list_columns(self, table):

		cursor = self.connection.execute("SELECT * FROM %s;" % table)
		
		return list(map(lambda x: x[0], cursor.description))

	def list_tables(self):

		command = "SELECT name FROM sqlite_master WHERE type='table';"
		tables = self.cursor.execute(command).fetchall()
		output = []
		for table in tables:
			output.append(table[0])
		
		return output

