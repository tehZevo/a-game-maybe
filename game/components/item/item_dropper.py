from game.ecs import Component
import game.components as C
from .dropped_item import DroppedItem
from game.utils.constants import ITEM_DROP_RADIUS
from game.utils import Vector

class ItemDropper(Component):
  def __init__(self):
    super().__init__()

  def drop(self, item, pos):
    #TODO: drop with random velocity?
    offset = Vector.random_disc(ITEM_DROP_RADIUS)
    dropped_item = self.entity.world.create_entity([
      C.Position(pos + offset),
      DroppedItem(item)
    ])
    return dropped_item
