import dearpygui.dearpygui as dpg
import dearpygui_extend as dpge

dpg.create_context()

layout='''
LAYOUT dashboard center center
	COL menu 0.2 center top
	COL content
		ROW 0.5
			COL main_content
		ROW 0.4
			COL grid 1
				ROW
					COL subcontent_A 0.33 center top
					COL subcontent_B 0.33 center top
					COL subcontent_C 0.33 center top
				ROW
					COL subcontent_D 0.33 center top
					COL subcontent_E 0.33 center top
					COL subcontent_F 0.33 center top
		ROW 0.1
			COL message_log
'''

with dpg.window(tag='main_window'):
	dpge.add_layout(layout, debug=True)

dpg.create_viewport()
dpg.set_primary_window('main_window', True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()