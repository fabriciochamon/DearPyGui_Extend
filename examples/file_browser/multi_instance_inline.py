import dearpygui.dearpygui as dpg
import dearpygui_extend as dpge

dpg.create_context()

def show_selected_file(sender, files, cancel_pressed, user_data):
	dpg.set_value(f'selected_file{user_data}', files[0])

with dpg.window(width=1000, height=1000, label='Multi inline file dialogs example'):
	for i in range(3):
		with dpg.group(horizontal=True):
			with dpg.group():
				dpg.add_text(f'File browser #{i+1}', color=(0,255,0))
				dpge.add_file_browser(
					width=500,
					height=300, 
					allow_multi_selection=False,
					selection_callback=show_selected_file,
					user_data=i)

			dpg.add_text(tag=f'selected_file{i}')

dpg.create_viewport()
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()