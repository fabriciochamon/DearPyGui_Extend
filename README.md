# DearPyGui_Extend
Extensions and custom widgets for [Dear Py GUI](http://github.com/hoffstadt/DearPyGui)

API Documentation: 
[dearpygui-extend.readthedocs.io](dearpygui-extend.readthedocs.io) [![Documentation Status](https://readthedocs.org/projects/dearpygui-extend/badge/?version=latest)](https://dearpygui-extend.readthedocs.io/en/latest/?badge=latest) 

## Movable Groups
Add Drag'n'drop ability to groups ("swap" or "replace" behaviors):

![](./resources/movable_groups.gif)

Usage:
```py
import dearpygui.dearpygui as dpg
import dearpygui_extend as dpge

with dpge.movable_group():
	dpg.add_text('Some text')
	...
```

or
```py
import dearpygui.dearpygui as dpg
import dearpygui_extend as dpge

win = dpg.add_window(tag='window1')
mg = dpge.add_movable_group(parent=win)
text = dpg.add_text('Some text', parent=mg)
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
from dearpygui_extend.file_browser import FileBrowser

filetype_filers = [
	{ 'label': 'All files', 'formats': ['*'] },
	{ 'label': 'Images', 'formats': ['jpg', 'png', 'gif'] },
]
FileBrowser(
	initial_path='~/Downloads/images',
	collapse_sequences=True,
	collapse_padding_str='#',
	show_hidden_files=False,
	filetype_filers=filetype_filers,
	path_input_style=FileBrowser.BREADCRUMB,
):
```