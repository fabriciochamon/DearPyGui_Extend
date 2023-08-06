import dearpygui.dearpygui as dpg
from dearpygui_extend.movable_group import MovableGroup

dpg.create_context()

# load example images
images = ['sphere','cube','tube','torus','cone']
with dpg.texture_registry():
	for image in images:
		width, height, channels, data = dpg.load_image(f'../_assets/{image}.png')
		dpg.add_static_texture(width=width, height=height, default_value=data, tag=image)

# validate user has selected all 3 cards
def on_drop(source, target):
	slot_list = dpg.get_item_children('slot_list', 1)[1:]
	containers = [dpg.get_item_children(x, 1)[0] for x in slot_list]
	texts = [dpg.get_item_children(x, 1)[0] for x in containers]
	selected = [dpg.get_value(x) for x in texts]
	if '' not in selected:
		dpg.set_value('status', 'Congratulations, you\'ve selected all 3 cards!'.upper())
		dpg.set_value('chosen_cards', selected)

# main window
with dpg.window(label='Example', width=400, pos=(0,20)):

	with dpg.group(horizontal=True):

		# available cards
		with dpg.group():
			dpg.add_text('Available Cards:')
			for i, image in enumerate(images):
				with MovableGroup(
					image, 
					width=100,
					drop_behavior=MovableGroup.REPLACE, 
					category='cards', 
					droppable_categories=[], 
					drop_callback=on_drop,
					on_drop_changes={
						'category': 'slots',
						'droppable_categories': ['slots','cards'],
						'drop_behavior': MovableGroup.SWAP
					},):

					dpg.add_image(image)

		# empty slots
		with dpg.group(tag='slot_list'):
			dpg.add_text('Selected Cards:')
			for i in range(3):
				with MovableGroup(
					title='', 
					width=100, 
					category='slots', 
					droppable_categories=['slots','cards']):

					dpg.add_text(f'[EMPTY SLOT {i+1}]')

	with dpg.group():
		dpg.add_text('', tag='status')
		dpg.add_text('', tag='chosen_cards')


# information window
with dpg.window(label='Info', width=400, pos=(410,20)):
	dpg.add_text('You can define "category" and "droppable_categories" to control where a group can be dropped', wrap=380)
	dpg.add_text('In this example, user is presented with a list of available cards (the "cards" category), and can choose 3 to add to Empty Slots (the "slots" category).', wrap=380)
	dpg.add_text('Images group:', wrap=350, indent=30)
	dpg.add_text('category             = "cards"', wrap=330, indent=50)
	dpg.add_text('droppable_categories = []', wrap=330, indent=50)
	dpg.add_text('* User is not allowed to rearrange left column', wrap=330, indent=50)
	dpg.add_text('Slots group:', wrap=350, indent=30)
	dpg.add_text('category             = "slots"', wrap=330, indent=50)
	dpg.add_text('droppable_categories = ["slots", "cards"]', wrap=330, indent=50)
	dpg.add_text('* User is allowed to rearrange right column and receive cards from left column', wrap=330, indent=50)
	dpg.add_separator()
	dpg.add_text('The cards can only be moved left to right, and when moved they also become a "slot" item, which can be dragged up/down.', wrap=380)
	dpg.add_separator()

dpg.create_viewport()
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()