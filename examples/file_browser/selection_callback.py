import dearpygui.dearpygui as dpg
import dearpygui_extend as dpge
from pathlib import Path

dpg.create_context()

def display_texture(sender, files):
	selection = Path(files[0])
	if selection.is_file():
		
		# register texture if not opened yet
		texture_name = selection.name
		if not dpg.does_item_exist(texture_name):
			width, height, channels, data = dpg.load_image(str(selection))
			with dpg.texture_registry():
				dpg.add_static_texture(width=width, height=height, default_value=data, tag=texture_name)

		# destroy/recreate the image widget
		if dpg.does_item_exist('image'):
			dpg.delete_item('image')
		dpg.add_image(texture_name, parent='tex_viewer', tag='image')

with dpg.window(width=600, height=550, label='Texture Viewer'):
	dpg.add_text('The filebrowser widget can be added inline (default) or as a separate window (show_as_window=True).', wrap=500)
	dpg.add_text('In this example added inline (for easy and constant access to files), and a simple image viewer is created tracking user selected files in realtime with the "selection_callback":', wrap=500)
	dpg.add_separator()
	
	with dpg.group():
		
		filetype_filter = [{'label': 'Images', 'formats': ['jpg','png','gif','bmp','psd']}]
		dpge.add_file_browser(
			selection_callback=display_texture,
			filetype_filter=filetype_filter,
			default_path=Path(__file__).parent.parent / '_assets',
			allow_multi_selection=False,
			collapse_sequences=False,
			collapse_sequences_checkbox=False,
			height=250
		)

	dpg.add_separator()
	dpg.add_text('Selected texture preview:')
	dpg.add_group(tag='tex_viewer')
		
dpg.create_viewport(width=1000)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()