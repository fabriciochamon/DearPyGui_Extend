import dearpygui.dearpygui as dpg
import dearpygui_extend as dpge

# init data
sample_data = [
	{'name': 'John',  'age': 31, 'document': None},
	{'name': 'Mark',  'age': 54, 'document': None},
	{'name': 'Laura', 'age': 37, 'document': None},
]

allowed_files = [
	{'label': 'Documents', 'formats': ['doc','pdf','txt','xls','rtf','html']}
]


dpg.create_context()

# callback
def set_document(sender, files, cancel_pressed, user_data):
	if not cancel_pressed:
		# display selected file
		dpg.set_value(f'document_{user_data}', files[0])

		# change text of filebrowser button
		dpg.configure_item(f'fb_document_{user_data}_button', label='Done! (click to select again)')

# UI
with dpg.window() as mainwin:
	dpg.add_text('User\'s documents:')
	with dpg.table(resizable=True, sortable=True, policy=dpg.mvTable_SizingStretchProp):

		# header
		for k in sample_data[0].keys():
			dpg.add_table_column(label=k.capitalize())
		
		# rows
		for i, person in enumerate(sample_data):
			with dpg.table_row():
				dpg.add_text(person['name'])
				dpg.add_text(person['age'])
				with dpg.group(horizontal=True):
					dpge.add_file_browser(
						tag=f'fb_document_{i}',
						default_path='~/Downloads',
						width=650,
						height=350,
						filetype_filter=allowed_files,
						show_ok_cancel=True, 
						collapse_sequences=False,
						collapse_sequences_checkbox=False, 
						allow_multi_selection=False,
						callback=set_document,
						user_data=i,
						show_as_window=True,
						)
					dpg.add_text(tag=f'document_{i}', default_value=f'allowed: {str(allowed_files[0]["formats"])}')


dpg.create_viewport(title='Multi filebrowser instances example', width=1200, height=500)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window(mainwin, True)
dpg.start_dearpygui()
dpg.destroy_context()