import dearpygui.dearpygui as dpg
import dearpygui_extend as dpge

dpg.create_context()

def add_selected_files_to_list_drag(sender, app_data, user_data):
	app_data = [item.replace('#', '\r#') for item in app_data]
	dpg.configure_item('selected_files', items=app_data)

def add_selected_files_to_list_callback(sender, files, cancel_pressed):
	if not cancel_pressed:
		files = [item.replace('#', '\r#') for item in files]
		dpg.configure_item('selected_files', items=files)

with dpg.window(width=800, height=800):
	with dpg.group(horizontal=True):
		dpg.add_color_picker(width=200, default_value=(255,124,30,255))
		dpge.add_file_browser(callback=add_selected_files_to_list_callback)
		
	with dpg.group(horizontal=True, width=-1):
		dpg.add_listbox(tag='selected_files', payload_type=dpge.file_browser.PAYLOAD_TYPE, num_items=10, drop_callback=add_selected_files_to_list_drag)


dpg.create_viewport(width=1920, height=1080)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()