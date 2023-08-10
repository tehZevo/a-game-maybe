from game.ecs import Component
from ..physics import Position

class TileEntity(Component):
  def __init__(self):
    super().__init__()
    self.require(Position)
    self.solid = False
