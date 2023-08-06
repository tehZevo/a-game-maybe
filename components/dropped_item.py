from ecs import Component
from components import Sprite

#TODO: ok so equipped items probably shouldnt have a position...

class DroppedItem(Component):
  def __init__(self, item):
    super().__init__()
    self.require(Sprite)
    self.item = item

  def start(self):
    self.get_component(Sprite).set_sprite(self.item.icon)
