import dearpygui.dearpygui as dpg
import dearpygui_extend as dpge

# make sure to avoid clashing tags on your layout text! there is NO error checking on dpge side!
layout_tab1='''
LAYOUT grid_3x3 center center
	ROW
		COL tab1_row1_col1
		COL tab1_row1_col2
		COL tab1_row1_col3
	ROW
		COL tab1_row2_col1
		COL tab1_row2_col2
		COL tab1_row2_col3
	ROW
		COL tab1_row3_col1
		COL tab1_row3_col2
		COL tab1_row3_col3
'''

layout_tab2='''
LAYOUT grid_2x2 center center
	ROW
		COL tab2_row1_col1
		COL tab2_row1_col2
	ROW
		COL tab2_row2_col1
		COL tab2_row2_col2
'''

# we store layout objects in a dict (keys = tab tags)
# we'll use this later for layout initialization when app starts (or when user clicks on one of the tabs)
layouts = {}

dpg.create_context()

with dpg.window(tag='main_window'):
	with dpg.tab_bar():

		tab_tag = 'tab1'
		with dpg.tab(tag=tab_tag, label='tab 1'):

			# IMPORTANT! layouts need to be a direct child of WINDOW or CHILD_WINDOW widgets
			with dpg.child_window():
				layout = dpge.add_layout(layout_tab1, debug=True)
				layouts[tab_tag] = layout
		
		tab_tag = 'tab2'				
		with dpg.tab(tag=tab_tag, label='tab 2'):

			# IMPORTANT! layouts need to be a direct child of WINDOW or CHILD_WINDOW widgets
			with dpg.child_window():
				layout = dpge.add_layout(layout_tab2, debug=True)	
				layouts[tab_tag] = layout


# ---- dpge LAYOUT INITIALIZATION ----#
def init_layouts(sender=None, app_data=None, user_data=None):
	global layouts

	# wait for one frame so dpg is able to compute widget sizes
	dpg.split_frame()

	# if clicked on a tab, init its layout
	if app_data:
		tab_tag = dpg.get_item_alias(app_data[1])
		layouts[tab_tag].init()

	# otherwise init all layouts
	else:
		for layout in layouts.values():
			layout.init()

# tab click handler
with dpg.item_handler_registry() as tab_handler:
	dpg.add_item_clicked_handler(callback=init_layouts)

# bind handler to all tabs
for tab in layouts.keys():
	dpg.bind_item_handler_registry(tab, tab_handler)

# run layout initialization upon app start (on frame 2)
# again we need to wait for 1 frame so dpg is able to compute widget sizes
dpg.set_frame_callback(2, init_layouts)

# ---- dpge LAYOUT INITIALIZATION ----#


dpg.create_viewport(title='Multiple layouts inside tabs example')
dpg.set_primary_window('main_window', True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()