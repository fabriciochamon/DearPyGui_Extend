import dearpygui.dearpygui as dpg
import dearpygui_extend as dpge

dpg.create_context()

layout='''
LAYOUT grid_3x3 center center
	ROW
		COL row1_col1
		COL row1_col2
		COL row1_col3
	ROW
		COL row2_col1
		COL row2_col2
		COL row2_col3
	ROW
		COL row3_col1
		COL row3_col2
		COL row3_col3
'''

# you can use the "height_factor" arg as a multiplier for the layout height inside its container (values: 0-1) 
with dpg.window(tag='main_window'):
	mylayout = dpge.add_layout(layout, debug=True, height_factor=0.98)

dpg.create_viewport()
dpg.set_primary_window('main_window', True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()