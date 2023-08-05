from ecs import Component
from components import Sprite, Item

#TODO: ok so equipped items probably shouldnt have a position...

class DroppedItem(Component):
  def __init__(self):
    super().__init__()
    self.require(Item)
    self.require(Sprite)

  def start(self):
    item = self.get_component(Item)
    sprite = self.get_component(Sprite)
    sprite.set_sprite(item.icon)
