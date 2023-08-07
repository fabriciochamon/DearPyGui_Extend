from .movable_group import MovableGroup

class movable_group(MovableGroup):
	pass

def add_movable_group(**kwargs):
	return MovableGroup(**kwargs).create_group()