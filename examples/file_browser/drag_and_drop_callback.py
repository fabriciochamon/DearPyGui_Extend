import dearpygui.dearpygui as dpg
import dearpygui_extend as dpge

dpg.create_context()

def add_selected_folders_to_list(sender, files):
	items = dpg.get_item_configuration('selected_files')['items']
	items.extend(files)
	items = list(set(items))
	dpg.configure_item('selected_files', items=items)

def clear_list():
	dpg.configure_item('selected_files', items=[])

with dpg.window(width=1000, height=800, label='Drag and drop example'):
	
	dpg.add_text('Drag and drop folders from the file browser onto the list on the right:')
	dpg.add_separator()

	with dpg.group(horizontal=True):
		dpge.add_file_browser(dirs_only=True, width=600)
		with dpg.group(width=400):
			dpg.add_text('Selected folders:')
			dpg.add_listbox(tag='selected_files', num_items=25, payload_type=dpge.file_browser.PAYLOAD_TYPE, drop_callback=add_selected_folders_to_list)
			dpg.add_button(label='clear list', callback=clear_list)

dpg.create_viewport()
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()