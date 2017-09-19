'''
Created By: Roman Beya
Created On: 19-Sep-2017
Created For: ICS3U
This program displays the name of the school and it's mascots
'''

import ui

def mths_touch_up_on_inside(sender):
	# This displays the name of the school and it's mascot
	view['schools_label'].text = ("St. Mother Teresa High School\nGo Titans!!")

def joes_touch_up_on_inside(sender):
	# This displays the name of the school and it's mascot
	view['schools_label'].text = ("St. Joes High School\nGo Jaguars!!")
	
def marks_touch_up_on_inside(sender):
	# This displays the name of the school and it's mascot
	view['schools_label'].text = ("St. Marks High School\nGo Lions!!")

view = ui.load_view()
view.present('sheet')
