# created by raymond octavious
# created on september 15, 2017
#created for ics3u
# created for daily assignment 
import ui

def english_touch_up_inside(sender):
	#displays english version
	view['hello_world_international_label'].text = ('hello, world!')

def french_touch_up_inside(sender):
	#displays french version
	view['hello_world_international_label'].text = ('bonjour, le monde!')
	
def spanish_touch_up_inside(sender):
	#displays spanish version
	view['hello_world_international_label'].text = ('hola, mundo!')
				
view = ui.load_view()
view.present('sheet')
