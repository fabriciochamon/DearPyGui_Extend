import dearpygui.dearpygui as dpg
import dearpygui_extend as dpge

dpg.create_context()

layout='''
LAYOUT example center top
	ROW 0.2
		COL top_menu 1 center center
	ROW
		COL resize_me_1
		COL resize_me_2
		COL resize_me_3
'''

with dpg.window(tag='main_window'):
	dpge.add_layout(layout, debug=True, resizable=True)


dpg.create_viewport()
dpg.set_primary_window('main_window', True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()