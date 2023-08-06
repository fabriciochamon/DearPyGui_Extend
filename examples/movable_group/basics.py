import dearpygui.dearpygui as dpg
from dearpygui_extend.movable_group import MovableGroup

dpg.create_context()

with dpg.window():

	dpg.add_text('Drag groups below to rearrange. You can drag from anywhere inside the group:')
	dpg.add_separator()

	with MovableGroup('Group 1'):
		dpg.add_input_text(label='username')
		dpg.add_input_text(label='password', password=True)
		dpg.add_button(label='Login')

	with MovableGroup('Group 2'):
		dpg.add_combo(label='choose', items=['Apples', 'Oranges', 'Bananas'])
		dpg.add_slider_int(label='Quantity', default_value=10)

	with MovableGroup('Group 3'):
		dpg.add_text('[Empty group]')

dpg.create_viewport()
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()