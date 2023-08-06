import dearpygui.dearpygui as dpg
from dearpygui_extend.movable_group import MovableGroup

dpg.create_context()

with dpg.window(label='window 1', width=300, pos=(0,10)):

	dpg.add_text('You can restrict moving groups within the same window only:', wrap=250)
	dpg.add_text('(Try moving any group to the other window)', wrap=250)
	
	dpg.add_separator()

	with MovableGroup('I only like my own window', same_window_only=True):
		dpg.add_color_picker()

	with MovableGroup('Yeah, me too', same_window_only=True):
		with dpg.table():
			dpg.add_table_column(label='col 1')
			dpg.add_table_column(label='col 2')
			for i in range(5):
				with dpg.table_row():
					dpg.add_text(f'cell {i*2}')
					dpg.add_text(f'cell {i*2+1}')

with dpg.window(label='window 2', width=300, pos=(320,10)):

	dpg.add_text('You can restrict moving groups within the same window only:', wrap=250)
	dpg.add_text('(Try moving any group to the other window)', wrap=250)
	
	dpg.add_separator()

	title_color = (0,255,0,255)
	with MovableGroup('I can\'t be moved to the left', same_window_only=True, title_color=title_color):
		dpg.add_button(label='A button')
		dpg.add_text('... and some text')

	with MovableGroup('Don\'t even try window 1', same_window_only=True, title_color=title_color):
		dpg.add_slider_floatx(label='vector1', size=3)
		dpg.add_slider_floatx(label='vector2', size=3)
		dpg.add_slider_floatx(label='vector3', size=3)


dpg.create_viewport()
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()