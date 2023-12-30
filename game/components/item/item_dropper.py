from game.ecs import Component
import game.components as C
from .dropped_item import DroppedItem

class ItemDropper(Component):
  def __init__(self):
    super().__init__()

  def drop(self, item, pos):
    #TODO: drop with random velocity?
    dropped_item = self.entity.world.create_entity([
      C.Position(pos),
      DroppedItem(item)
    ])
    return dropped_item
