import dearpygui.dearpygui as dpg
import dearpygui_extend as dpge

dpg.create_context()

with dpg.window(width=300):

	dpg.add_text('Drag groups below to rearrange. You can drag from anywhere inside the group:', wrap=290)
	dpg.add_separator()

	with dpge.movable_group('Group 1'):
		dpg.add_input_text(label='username')
		dpg.add_input_text(label='password', password=True)
		dpg.add_button(label='Login')

	with dpge.movable_group('Group 2'):
		dpg.add_combo(label='choose', items=['Apples', 'Oranges', 'Bananas'])
		dpg.add_slider_int(label='Quantity', default_value=10)

	with dpge.movable_group('Group 3'):
		dpg.add_text('[Empty group]')

dpg.create_viewport()
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()