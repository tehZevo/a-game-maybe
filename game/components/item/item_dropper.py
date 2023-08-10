from game.ecs import Component
from ..physics import Position
from .dropped_item import DroppedItem

class ItemDropper(Component):
  def __init__(self):
    super().__init__()

  def drop(self, item, pos):
    #TODO: drop with random velocity?
    self.entity.world.create_entity([
      Position(pos),
      DroppedItem(item)
    ])
