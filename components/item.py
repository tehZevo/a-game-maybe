from ecs import Component
from components import Position, Sprite

#TODO: where to store drop rate?

class Item(Component):
  def __init__(self):
    super().__init__()
    self.require(Sprite)

  def start(self):
    self.get_component(Sprite).set_sprite("assets/item.png")
