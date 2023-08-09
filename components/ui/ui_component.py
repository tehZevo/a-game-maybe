from ecs import Component, World
from components.physics.position import Position
from components.core.drawable import Drawable

class UIComponent(Component, Drawable):
  def __init__(self):
    super().__init__()
    self.require(Position)
