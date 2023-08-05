from ecs import Component
from components import Position, Sprite, DroppedItem

class ItemDropper(Component):
  def __init__(self):
    super().__init__()

  def drop(self, item_component_type, pos):
    self.entity.world.create_entity([
      Position(pos),
      item_component_type(),
      DroppedItem()
    ])
