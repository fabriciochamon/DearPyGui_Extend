# DearPyGui_Extend
Extensions and custom widgets for [Dear Py GUI](http://github.com/hoffstadt/DearPyGui)

## Movable Groups
Add Drag'n'drop ability to groups ("swap" or "replace" behaviors):

![](./resources/movable_groups.gif)

Usage:
```py
import dearpygui_extend as dpge

with dpge.MovableGroup():
	# regular dpg UI layout
	dpg.add_text('Some text')
	...
```
</br>

## Extended file browser
Features:

* Supports **file sequence** (collapsed) entries:
	`image.001.jpg, image.002.jpg, image.003.jpg --> 'image.###.jpg (001-003)'`
* Multi-selection (pick single or multiple files/sequences)
* Click Breadcrumb path for folder quick access, double click to manually edit path
* File filters: by name, type
* Sorting (smart size and date for collapsed sequences)
* Draggable files (ability to expand sequences on a drop callback)

> [!NOTE]
> Requires [Fileseq](https://pypi.org/project/Fileseq/) package: `pip install fileseq`

![](./resources/fileseq_browser.gif)
Usage:
```py
import dearpygui_extend as dpge

filetype_filers = [
	{ 'label': 'All files', 'formats': ['*'] },
	{ 'label': 'Images', 'formats': ['jpg', 'png', 'gif'] },
]
filebrowser = dpge.FileBrowser(
	initial_path='~/Downloads/images',
	collapse_sequences=True,
	collapse_padding_str='#',
	show_hidden_files=False,
	filetype_filers=filetype_filers,
	path_input_style=dpge.FileBrowse.BREADCRUMB,
):
```