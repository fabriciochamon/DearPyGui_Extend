from .movable_group import MovableGroup

class movable_group(MovableGroup):
	pass

def add_movable_group(**kwargs):
	"""
	A group with drag'n'drop/moving capabilities

	:param str title: Group title (shown at the top)
	:param int width: Item width
	:param int height: Item height
	:param tuple title_color: Title color (an item theme will be created and assigned, making sure we only have a single theme per unique color of all movable groups)
	:param bool same_window_only: Only allows this group to be moved within its parent window.
	:param int drop_behavior: The default action for when a movable group is dropped onto another group. (movable_group.SWAP or movable_group.REPLACE)
	:param str category: The group category. Categories can be used in conjunction with "droppable_categories" to filter where a movable_group can be dropped.
	:param list droppable_categories: The list of categories allowed to be dropped onto this group. 
	:param dict on_drop_changes: The contents of this dict will be applied whenever this group is dropped (dict keys should match movable_group() arguments). You can use this to change a group category after the group is moved, for example.
	:param callable drop_callback: Callback executed when group is moved. Args "source" and "target" are available.
	:param any user_data: Additional user_data. Because movable_group() takes over the "user_data" arg for internal manipulations, you'll need to access your group user_data inside the 'user' sub-key: item['user_data']['user']
	:param int parent: The group parent item.

	:returns: A dearpygui item id
	"""
	return MovableGroup(**kwargs).create_group()