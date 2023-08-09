import dearpygui.dearpygui as dpg
import dearpygui_extend as dpge
import inspect

dpg.create_context()

filebrowser = None
def config_filebrowser(sender, app_data, user_data):
	
	# build browser
	global filebrowser
	kwargs = {}
	kwargs_remove = ['self', 'parent', 'filetype_filter', 'filetype_filter_default', 'expand_sequences_on_callback', 'callback', 'selection_callback']
	signature = inspect.signature(dpge.file_browser.__init__)
	for k,v in signature.parameters.items():
		if k not in kwargs_remove: 
			kwargs[k]=dpg.get_value(k) if dpg.get_value(k) is not None else v.default
			if k=='label':
				kwargs[k]=(dpg.get_value('label_button'), dpg.get_value('label_dialog'))
				if (dpg.get_value('label_button'), dpg.get_value('label_dialog'))==('',''):
					kwargs[k]='Choose files'
			if k=='path_input_style':
				kwargs[k]=['file_browser.PATH_INPUT_STYLE_TEXT_ONLY', 'file_browser.PATH_INPUT_STYLE_BREADCRUMB', 'file_browser.PATH_INPUT_STYLE_BOTH'].index(dpg.get_value('path_input_style'))

	if dpg.does_item_exist('fb_window'): 
		for popup in filebrowser.popups_created:
			if dpg.does_item_exist(popup): dpg.delete_item(popup)		
		dpg.delete_item('fb_window')
		dpg.delete_item('dpge_filebrowser_window')
	dpg.add_window(tag='fb_window', width=kwargs['width'], height=kwargs['height'], label=dpg.get_value('label_dialog'), pos=(510, 10))

	filebrowser = dpge.add_file_browser(parent='fb_window', **kwargs)
	
	# build func call
	args='\n'
	for k,v in kwargs.items():
		args += '\t'
		args += k+'='
		args += '\'' if isinstance(v, str) else ''
		args += str(v)
		args += '\'' if isinstance(v, str) else ''
		args += ', \n'
	function_call = f'dpge.add_file_browser({args})'
	dpg.set_value('function_call', function_call)

def pick_icon(icon):
	dpg.set_value('label_button', icon)
	dpg.configure_item('popup_icon', show=False)


# MAIN
with dpg.window(tag='configurator', width=500, height=900, label='File browser configurator', pos=(0, 10)):
	with dpg.group(horizontal=True):
		dpg.add_input_int(tag='width', label='width', default_value=600, width=100, step=100)
		dpg.add_input_int(tag='height', label='height', default_value=500, width=100, step=100)
	
	dpg.add_input_text(tag='label_button', label='label (button)', default_value='Choose files')
	with dpg.tooltip(dpg.last_item()):
		dpg.add_text('Text displayed inside a file chooser button, if "show_as_window==True".')
		dpg.add_text('Can optionally display a single icon instead (right click this text box to choose icon)')
	with dpg.popup(parent='label_button', tag='popup_icon', mousebutton=dpg.mvMouseButton_Right):
		dpg.add_button(label='Folder icon', callback=lambda: pick_icon('dpge_filebrowser_icon_folder'))
		dpg.add_button(label='File icon', callback=lambda: pick_icon('dpge_filebrowser_icon_file'))
		dpg.add_button(label='Files icon', callback=lambda: pick_icon('dpge_filebrowser_icon_dragfiles'))
		
	dpg.add_input_text(tag='label_dialog', label='label (dialog)', default_value='Select files or folders')
	with dpg.tooltip(dpg.last_item()):
		dpg.add_text('Text displayed as the filebrowser window label, if "show_as_window==True"')

	with dpg.group(horizontal=True):
		dpg.add_checkbox(tag='show_as_window', label='Show as window', default_value=False)
		with dpg.tooltip(dpg.last_item()):
			dpg.add_text('The filebrowser can be displayed inline or as a separate window. If "show_as_window==True" only a button widget is displayed inline, and the full filebrowser window is shown when user clicks the button. (See "label" for more info)', wrap=400)
		dpg.add_checkbox(tag='modal_window', label='Modal window', default_value=False)
	
	dpg.add_input_text(tag='default_path', label='default_path', default_value='~')
	with dpg.tooltip(dpg.last_item()):
		dpg.add_text('Accepts absolute or relative paths.')
		dpg.add_text('(and will always expand the user home folder "~")')

	with dpg.group(horizontal=True):
		dpg.add_checkbox(tag='collapse_sequences', label='Collapse sequences', default_value=True)
		with dpg.tooltip(dpg.last_item()):
			dpg.add_text('Should the filebrowser collapse sequences by default ?')
		dpg.add_checkbox(tag='collapse_sequences_checkbox', label='Collapse sequences checkbox', default_value=True)
		with dpg.tooltip(dpg.last_item()):
			dpg.add_text('Controls the visibility of the "collapse sequences" checkbox inside the filebrowser')

	dpg.add_input_text(tag='sequence_padding', label='Sequence padding', default_value='#', width=50)
	with dpg.tooltip(dpg.last_item()):
		dpg.add_text('Padding mask to represent frame numbers in collapsed sequences. (example: "#" --> "MyImage.####.png")')

	dpg.add_checkbox(tag='show_hidden_files', label='Show hidden files', default_value=False)
	with dpg.tooltip(dpg.last_item()):
			dpg.add_text('Show files and folders starting with \'.\' ? ')

	dpg.add_combo(tag='path_input_style', label='Path input style', items=['file_browser.PATH_INPUT_STYLE_TEXT_ONLY', 'file_browser.PATH_INPUT_STYLE_BREADCRUMB', 'file_browser.PATH_INPUT_STYLE_BOTH'], default_value='file_browser.PATH_INPUT_STYLE_BREADCRUMB')
	with dpg.tooltip(dpg.last_item()):
		dpg.add_text('How the user will input the current directory') 
		dpg.add_text('If "BREADCRUMB", user can always double click path parts to manually enter the path') 

	with dpg.group(horizontal=True):
		dpg.add_checkbox(tag='add_filename_tooltip', label='Add filename tooltip', default_value=False)
		dpg.add_input_int(tag='tooltip_min_length', label='Tooltip min length', default_value=100, width=90, step=10)
		with dpg.tooltip(dpg.last_item()):
			dpg.add_text('Minimum filename length to be displayed as tooltip.')
		
	dpg.add_input_float(tag='icon_size', label='Icon size', default_value=1, width=100, step=0.1)
	with dpg.tooltip(dpg.last_item()):
		dpg.add_text('Built-in icons size multiplier')

	dpg.add_checkbox(tag='dirs_only', label='Dirs only', default_value=False)
	with dpg.tooltip(dpg.last_item()):
		dpg.add_text('Show directories only')
	dpg.add_checkbox(tag='allow_multi_selection', label='Allow multi selection', default_value=True)
	with dpg.tooltip(dpg.last_item()):
		dpg.add_text('Allow multiple file selection with CTRL/SHIFT keys')

	dpg.add_checkbox(tag='allow_drag', label='Allow drag files', default_value=True)
	with dpg.tooltip(dpg.last_item()):
		dpg.add_text('Add file dragging behavior to be used with drop_callbacks')
		dpg.add_text('(payload_type = "file_browser.PAYLOAD_TYPE")')

	dpg.add_checkbox(tag='allow_create_new_folder', label='Allow create new folder', default_value=True)
	with dpg.tooltip(dpg.last_item()):
		dpg.add_text('Only works when "show_nav_icons=True"')

	dpg.add_checkbox(tag='show_ok_cancel', label='Show OK/Cancel buttons', default_value=False)
	with dpg.tooltip(dpg.last_item()):
		dpg.add_text('Display action buttons at the bottom. Result of "callback" happens when user clicks these buttons. (Alternatively, leave this option off and work with draggable items using "allow_drag" and drop_callbacks instead)', wrap=400)
		
	dpg.add_checkbox(tag='show_nav_icons', label='Show navigation icons', default_value=True)
	with dpg.tooltip(dpg.last_item()):
		dpg.add_text('Display top navigation icons ("<", "^", "create folder", "home"). They can take considerable UI space depending on parent container size, so disabling this helps vizualize more of the current path being browsed.', wrap=400)


	dpg.add_spacer(height=15)
	dpg.add_button(label='Create filebrowser', callback=config_filebrowser)
	with dpg.tooltip(dpg.last_item()):
		dpg.add_text("IMPORTANT: due to how this configurator is made, you won't be able to navigate through the folders or click to edit the path. This is by design, but the resulting function call below will produce a perfectly working file browser widget on another .py file.", wrap=400)
	dpg.add_separator()
	dpg.add_spacer(height=15)

	dpg.add_text('This filebrowser\'s function call:')
	dpg.add_input_text(tag='function_call', multiline=True, width=450, height=300, indent=5)

# theme
with dpg.theme() as container_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (100, 100, 100))
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5)
    with dpg.theme_component(dpg.mvCheckbox):
        dpg.add_theme_color(dpg.mvThemeCol_CheckMark, (10, 10, 10))
    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 16, 16)


dpg.bind_item_theme('configurator', container_theme)

dpg.create_viewport(height=930)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()