from game.ecs import Component, World
from ..physics import Position
from . import Drawable

class UIComponent(Component, Drawable):
  def __init__(self):
    super().__init__()
    self.require(Position)
