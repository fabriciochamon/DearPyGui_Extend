import dearpygui.dearpygui as dpg
import dearpygui_extend as dpge
from pathlib import Path

dpg.create_context()

def expand_sequence_into_list(sender, files, cancel_pressed):
	if not cancel_pressed:
		files = [item.replace('#', '\r#') for item in files]
		dpg.configure_item('selected_files', items=files)
		dpg.set_value('status_selection', f'Expanded files: {len(files)}')

def clear_list():
	dpg.configure_item('selected_files', items=[])
	dpg.set_value('status_selection', 'Expanded files: 0')

with dpg.window(width=800, height=400, label='Expanding collapsed image sequences example'):
	dpge.add_file_browser(
		callback=expand_sequence_into_list,
		show_as_window=True,
		show_ok_cancel=True,
		label=('Choose image sequence ...', 'Select one or more files or sequences'),
		default_path='../_assets/image_sequence',
		height=600
		)

	dpg.add_text('Expanded files: 0', tag='status_selection')
	dpg.add_listbox(tag='selected_files', width=-1, num_items=12, payload_type=dpge.file_browser.PAYLOAD_TYPE)
	dpg.add_button(label='clear list', callback=clear_list)

dpg.create_viewport()
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()