import dearpygui.dearpygui as dpg
import dearpygui_extend as dpge

dpg.create_context()

def show_selected_file(sender, files, cancel_pressed):
	if not cancel_pressed:
		dpg.set_value('selected_file', files[0])

with dpg.window(width=400, label='Simple file dialog example'):
	dpge.add_file_browser(
		width=800,
		height=600,
		show_as_window=True, 
		show_ok_cancel=True, 
		allow_multi_selection=False, 
		collapse_sequences=True,
		callback=show_selected_file)

	dpg.add_text(tag='selected_file')

dpg.create_viewport()
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()