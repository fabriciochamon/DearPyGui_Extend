import dearpygui.dearpygui as dpg

class MovableGroup:
   # drop behavior constants
   SWAP    = 0
   REPLACE = 1  # (deletes target group)

   def __init__(
      self, 
      title='Group', 
      width=200, 
      height=100, 
      title_color=(0, 120, 180, 255), 
      same_window_only=False, 
      drop_behavior=SWAP, 
      category=None, 
      droppable_categories=None, 
      on_drop_changes=None,
      drop_callback=None,
      user_data=None,
      parent=None
      ):

      self.title = title   
      self.width = width
      self.height = height
      self.group = None   
      self.title_color = title_color
      self.same_window_only = same_window_only
      self.drop_behavior = drop_behavior
      self.category=category
      self.droppable_categories=droppable_categories
      self.on_drop_changes=on_drop_changes
      self.drop_callback=drop_callback
      self.extra_user_data=user_data
      self.all_user_data=None
      self.parent=parent
      self._payload_name = '_dpge_movable_group'
      self._theme_name = f'_dpge_movable_group_title_theme__{"_".join([str(x) for x in self.title_color])}'

      # add new title theme if it doesn't exist
      theme_exists = dpg.does_item_exist(self._theme_name)
      if not theme_exists:
         with dpg.theme(tag=self._theme_name):
            with dpg.theme_component(dpg.mvText):
               dpg.add_theme_color(dpg.mvThemeCol_Text, self.title_color)

      # append user_data to internal user_data:
      internal_user_data = self.__dict__
      internal_user_data['user']=self.extra_user_data
      self.all_user_data=internal_user_data

   def create_group(self):
      self.title = self.title or ''
      if self.parent:
         container = dpg.add_group(parent=self.parent)
      else:
         container = dpg.add_group()
      self.group = dpg.add_group(parent=container, width=self.width, height=self.height, drop_callback=self.move, payload_type=self._payload_name, user_data=self.all_user_data)
      title_text = dpg.add_text(self.title, parent=self.group)
      with dpg.tooltip(parent=title_text):
         dpg.add_text(f'Drag to move group "{self.title}"')
         dpg.bind_item_theme(title_text, self._theme_name)
      with dpg.drag_payload(parent=self.group, payload_type=self._payload_name, drag_data=self.all_user_data):
         dpg.add_text(f'Move "{self.title}"')
      return self.group

   def __enter__(self):
      self.create_group()      
      dpg.push_container_stack(self.group)
      return self.group
  
   def __exit__(self, exc_type, exc_val, exc_tb):
      dpg.pop_container_stack()
      with dpg.drag_payload(parent=self.group, payload_type=self._payload_name, drag_data=self.all_user_data):
         dpg.add_text(f'Move "{self.title}"')

   def move(sender, app_data, user_data):
      
      def get_item_window(item):
         parent = dpg.get_item_parent(item)
         parent_type = dpg.get_item_type(parent) if parent else None
         win = parent if parent_type=='mvAppItemType::mvWindowAppItem' else None
         while win is None:
            win = get_item_window(parent)
         return win
      
      source        = user_data['group']
      source_parent = dpg.get_item_parent(source)
      target        = app_data
      target_parent = dpg.get_item_parent(target)
      
      same_window = user_data['same_window_only']
      drop_behavior = user_data['drop_behavior']
      category = user_data['category']
      droppable_categories = dpg.get_item_configuration(target)['user_data']['droppable_categories']
      on_drop_changes = user_data['on_drop_changes']
      drop_callback = user_data['drop_callback']

      if not isinstance(droppable_categories, list) or (isinstance(droppable_categories, list) and category in droppable_categories):
         if source!=target:
            if not same_window or (same_window and get_item_window(source)==get_item_window(target)):

               # move group
               dpg.move_item(source, parent=target_parent)
               if drop_behavior==MovableGroup.SWAP:
                  dpg.move_item(target, parent=source_parent)
               elif drop_behavior==MovableGroup.REPLACE:
                  dpg.delete_item(target)

               # on drop changes
               if on_drop_changes:
                  for k,v in on_drop_changes.items():
                     if k in user_data.keys():
                        user_data[k] = v
                  dpg.configure_item(source, user_data=user_data)                
               
               # drop callback 
               if drop_callback: 
                  if drop_callback.__code__.co_argcount==0: drop_callback()
                  if drop_callback.__code__.co_argcount==1: drop_callback(source)
                  if drop_callback.__code__.co_argcount==2: drop_callback(source, target)
