from .movable_group import MovableGroup
from .file_browser import FileBrowser
from .layout import Layout 

class movable_group(MovableGroup):
	pass

def add_movable_group(**kwargs):
	"""
	A group with drag'n'drop/moving capabilities

	:param str title: Group title (text widget shown at the top).
	:param int width: Item width.
	:param int height: Item height.
	:param tuple title_color: Title color (a simple item theme is internally assigned to the group title)
	:param bool same_window_only: Only allow the group to be moved within its parent window.
	:param int drop_behavior: The default action for when a movable group is dropped onto another group. (movable_group.SWAP or movable_group.REPLACE)
	:param str category: The group category. Categories can be used in conjunction with "droppable_categories" to filter where a movable_group can be dropped.
	:param list droppable_categories: The list of categories allowed to be dropped onto this group. 
	:param dict on_drop_changes: The contents of this dict will be applied whenever this group is dropped over another group (dict keys should match movable_group() arguments). You can use this to change a group category after the group is moved, for example.
	:param callable drop_callback: Callback executed when group is moved. Args "source" and "target" are available.
	:param any user_data: Additional user_data. Because movable_group() takes over the "user_data" arg for internal manipulations, you'll need to access your group user_data inside the 'user' sub-key: item['user_data']['user']
	:param int parent: The group parent item.

	:returns: A dearpygui item id
	"""
	return MovableGroup(**kwargs).create_group()


class file_browser(FileBrowser):
	pass

def add_file_browser(**kwargs):
	"""
	A custom file browser with support for collapsed file sequences and extended functionality.

	:param str|tuple|list label: Label shown at window title and button widget (if "show_as_window" == True). Can be defined separately as a tuple/list of length 2: ('label on button', 'label on filebrowser window'). Accepts constants: file_browser.ICON_FILE, file_browser.ICON_FILES, file_browser.ICON_FOLDER to show built-in icons as an image button instead of a label.
	:param int width: Item width
	:param int height: Item height
	:param int parent: The filebrowser parent item
	:param str default_path: Initial path (filebrowser will expand user home folder '~', if present)
	:param bool collapse_sequences: Collapse numbered file sequences into a single entry.
	:param bool collapse_sequences_checkbox: Displays the checkbox option to turn on/off display of collapsed sequences.
	:param str sequence_padding: Padding mask to represent frame numbers in collapsed sequences. (example: "#" --> "MyImage.####.png")
	:param bool show_hidden_files: Display hidden files and folders (starting with ".")
	:param int path_input_style: How the user will input the filebrowser directory: file_browser.PATH_INPUT_STYLE_TEXT_ONLY, file_browser.PATH_INPUT_STYLE_BREADCRUMB, file_browser.PATH_INPUT_STYLE_BOTH
	:param bool add_filename_tooltip: Adds a tooltip to help visualizing large filenames (if file name exceeds "tooltip_min_length")
	:param int tooltip_min_length: Minimum filename length to be displayed as tooltip.
	:param int icon_size: Built-in icons size multiplier
	:param list filetype_filter: A list (of dicts) for the allowed file extensions combo. Expected format of each list item is: {'label': 'Images', formats: ['png', 'jpg', 'svg']}
	:param int filetype_filter_default: The default selected element from "filetype_filter" list
	:param int expand_sequences_on_callback: Expands collapsed sequences to multiple files when sending values to callbacks
	:param bool allow_multi_selection: Allow user to select multiples files/folders
	:param bool allow_drag: Allow files/folders to be dragged to other UI elements.
	:param bool allow_create_new_folder: Displays an icon to create a new folder on the header
	:param bool dirs_only: List directories only
	:param bool show_as_window: The filebrowser can be displayed inline or as a separate window. If "show_as_window==True" only a button widget is displayed inline, and the full filebrowser window is shown when user clicks the button. (See "label" for more info)
	:param bool modal_window: Create a modal window if "show_as_window"==True ? (IMPORTANT: currently there is a bug where the "allow_create_new_folder" popup will not display on a modal window!)
	:param bool show_ok_cancel: Display action buttons at the bottom. Result of "callback" happens when user clicks these buttons. (Alternatively, leave this option off and work with draggable items using "allow_drag" and drop_callbacks instead)
	:param bool show_nav_icons: Display top navigation icons ("<", "^", "create folder", "home"). They can take considerable UI space depending on parent container size, so disabling this might help vizualize more of the current path being browsed.
	:param callable callback: Callback executed when OK/Cancel buttons are pressed (if "show_ok_cancel==True"). Args "sender"(int), "files"(list) and "cancel_pressed"(bool) are available.
	:param callable selection_callback: Callback executed when user selects files/folders inside the browser. Args "sender"(int), "files"(list) are available.

	:returns: A FileBrowser object. You can access the "root" class attribute to refer to the top most dpg item of the FileBrowser.
	"""
	return FileBrowser(**kwargs)


class layout(Layout):
	pass

def add_layout(layout, **kwargs):
	"""
	A window layouting system based on a simple human readable format.

	:param str layout: A string containing the layout. Uses tab based identation syntax (More info below).
	:param int parent: The layout parent item.
	:param bool border: Displays a border around panes.
	:param bool resizable: Allow pane columns to be resized.
	:param bool debug: Displays random colors as indication for each pane.

	:returns: A Layout object. You can access the "root" class attribute to refer to the top most dpg item of the layout.

	LAYOUT - the top most item (required as the first line). Accepts 3 positional parameters: 
		- name: the main layout table tag
		- halign: horizontal alignment mode  (left | center | right)
		- valign: vertical alignment mode    (top  | center | bottom)
		
		*If defined, global layout alignment options will be used for all columns. (Any column can override this value with its own alignment parms).
	
	ROW - a row item. Accepts 1 positional parameter: 
		- size: row height as a normalized 0-1 value. (If omitted, remaining height will be automatically distributed between all the rows without this parm)
	
	COL - a column item. Accepts 4 positional parameters: 
		- name: the dpg container tag, that you can access later to put the child widgets on.
		- size: the column width as a normalized 0-1 value. (If omitted, remaining width will be automatically distributed between all the columns without this parm)
		- halign: horizontal alignment mode  (left | center | right)
		- valign: vertical alignment mode    (top  | center | bottom)

	"""
	return Layout(layout, **kwargs)