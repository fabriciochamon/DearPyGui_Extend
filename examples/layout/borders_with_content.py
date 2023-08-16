import dearpygui.dearpygui as dpg
import dearpygui_extend as dpge

dpg.create_context()

layout='''
LAYOUT example
	COL left_menu 0.2 left top
	COL content 0.6
		ROW 0.7
			COL node_editor 1 center center
		ROW 0.2
			COL nodes_cat_A
			COL nodes_cat_B
		ROW 0.1
			COL status_bar 1 left center
	COL tools 0.2 center top
'''

with dpg.window(tag='main_window'):
	dpge.add_layout(layout, debug=False, resizable=True, border=True)

# themes
with dpg.theme() as menu_theme:
	with dpg.theme_component(dpg.mvButton):
		dpg.add_theme_color(dpg.mvThemeCol_Button, (252, 186, 3))
		dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (255, 220, 50))
		dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (255, 255, 255))
		dpg.add_theme_color(dpg.mvThemeCol_Text, (10, 10, 10))
with dpg.theme() as tools_theme:
	with dpg.theme_component(dpg.mvButton):
		dpg.add_theme_color(dpg.mvThemeCol_Button, (0, 255, 110))
		dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (50, 255, 160))
		dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (255, 255, 255))
		dpg.add_theme_color(dpg.mvThemeCol_Text, (10, 10, 10))		
with dpg.theme() as status_theme:
	with dpg.theme_component(dpg.mvText):
		dpg.add_theme_color(dpg.mvThemeCol_Text, (100,100,100))


# LEFT MENU
with dpg.group(parent='left_menu', indent=5) as left_menu:
	dpg.add_text('MENU:')
	dpg.add_button(label='New graph', width=-1)
	dpg.add_button(label='Save graph as...', width=-1)
	dpg.add_button(label='Open Recent', width=-1)
dpg.bind_item_theme(left_menu, menu_theme)

# TOOLS RIGHT MENU
with dpg.group(parent='tools', indent=5) as tools:
	dpg.add_text('NODE TOOLS:')
	dpg.add_button(label='Rearrange nodes', width=-1)
	dpg.add_button(label='Copy nodes', width=-1)
	dpg.add_button(label='Paste nodes', width=-1)
	dpg.add_button(label='Group nodes', width=-1)
	dpg.add_button(label='Ungroup nodes', width=-1)
	dpg.add_separator()
	dpg.add_text('GRAPH TOOLS:')
	dpg.add_button(label='Clear graph', width=-1)
	dpg.add_button(label='Duplicate graph', width=-1)
	dpg.add_button(label='Disconnect all inputs', width=-1)
dpg.bind_item_theme(tools, tools_theme)	

# STATUS BAR
with dpg.group(parent='status_bar', indent=20) as status:
	dpg.add_text('Status:')
	dpg.bind_item_theme(dpg.last_item(), status_theme)	
	dpg.add_text('This is a message log. Maybe add node connection status upon editing the graph...')

# NODES CATEGORY A
with dpg.group(parent='nodes_cat_A', indent=20) as ndo_cat_A:
	dpg.add_spacer(height=10)
	dpg.add_text('Geometry Nodes:')
	dpg.add_separator()
	dpg.add_selectable(label='Sphere')
	dpg.add_selectable(label='Box')
	dpg.add_selectable(label='Torus')
	dpg.add_selectable(label='Cone')
	dpg.add_selectable(label='Tube')
	dpg.add_selectable(label='Platonic solids')

# NODES CATEGORY B
with dpg.group(parent='nodes_cat_B', indent=20) as ndo_cat_B:
	dpg.add_spacer(height=10)
	dpg.add_text('Modifier Nodes:')
	dpg.add_separator()
	dpg.add_selectable(label='Extrude')
	dpg.add_selectable(label='Revolve')
	dpg.add_selectable(label='Bend')
	dpg.add_selectable(label='Lattice')
	dpg.add_selectable(label='Deform by curve')

# NODE GRAPH EDITOR
with dpg.group(parent='node_editor', indent=5) as node_editor:
	dpg.add_text('Editing: "Scene.graph"')
	with dpg.node_editor():
		with dpg.node(label='Torus') as node_torus:
			with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Input):
				 dpg.add_input_float(label='radius', width=100, default_value=0.25)
			with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Output) as torus_out:
				 dpg.add_input_text(label='out', width=100)
		dpg.set_item_pos(node_torus, pos=(50, 50))

		with dpg.node(label='Bend modifier') as node_bend:
			with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Input) as bend_in:
				 dpg.add_input_text(label='In geo', width=100)
			with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Output):
				 dpg.add_input_text(label='out deformed', width=100)
		dpg.set_item_pos(node_bend, pos=(300, 150))

		dpg.add_node_link(torus_out, bend_in)

dpg.create_viewport(title='3D Scene graph editor (sample layout)')
dpg.set_primary_window('main_window', True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()