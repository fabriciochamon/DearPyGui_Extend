import dearpygui.dearpygui as dpg
import dearpygui_extend as dpge
import pprint

dpg.create_context()

def show_user_data(sender, app_data, user_data):
	group = user_data
	iternal_user_data = dpg.get_item_configuration(group)['user_data']
	user_user_data    = dpg.get_item_configuration(group)['user_data']['user']
	dpg.set_value('internal_user_data', pprint.pformat(iternal_user_data))
	dpg.set_value('user_user_data',     pprint.pformat(user_user_data))

with dpg.window(width=400, height=600):

	dpg.add_text('Because MovableGroups() take over the "user_data" arg for internal manipulations, you\'ll need to access your own user_data in an extra ["user"] subkey. Click button to see and example:', wrap=380)
	dpg.add_separator()

	with dpge.movable_group('Group 1', user_data='This is the actual group user_data!') as group:
		dpg.add_button(label='Click to show "user_data"', callback=show_user_data, user_data=group)
		dpg.add_separator()
		dpg.add_text('Result of: item_configuration["user_data"]')
		dpg.add_text(tag='internal_user_data', wrap=300, indent=20)
		dpg.add_separator()
		dpg.add_text('Result of: item_configuration["user_data"]["user"]')
		dpg.add_text(tag='user_user_data', wrap=300, indent=20)

dpg.create_viewport()
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()