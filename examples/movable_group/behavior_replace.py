import dearpygui.dearpygui as dpg
import dearpygui_extend as dpge

dpg.create_context()

with dpg.window():

	dpg.add_text('Control the drop behavior with constants: "MovableGroup.SWAP" and "MovableGroup.REPLACE"', wrap=350)
	dpg.add_separator()

	with dpge.movable_group('Group SWAPPABLE'):
		dpg.add_text('Dragging this group will swap contents with the target group. This is the default behavior.', wrap=200)

	with dpge.movable_group('Group dummy1'):
		dpg.add_button(label='button')

	# GROUP WITH "REPLACE" DROP BEHAVIOR
	with dpge.movable_group('Group REPLACEABLE', drop_behavior=dpge.movable_group.REPLACE):
		dpg.add_text('Dragging this group REPLACES (deletes) the target group.', wrap=200)

	with dpge.movable_group('Group dummy2'):
		with dpg.table(header_row=False):
			dpg.add_table_column()
			dpg.add_table_column()
			for i in range(5):
				with dpg.table_row():
					dpg.add_text(f'cell {i*2}')
					dpg.add_text(f'cell {i*2+1}')

dpg.create_viewport()
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()