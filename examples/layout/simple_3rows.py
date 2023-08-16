import dearpygui.dearpygui as dpg
import dearpygui_extend as dpge

dpg.create_context()

layout='''
LAYOUT simple_layout center center
	ROW
		COL row_A
	ROW
		COL row_B
	ROW
		COL row_C
'''

with dpg.window(tag='main_window'):
	dpge.add_layout(layout, debug=True)


dpg.create_viewport()
dpg.set_primary_window('main_window', True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()