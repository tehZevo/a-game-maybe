from ecs import Component
from components import Position

class TileEntity(Component):
  def __init__(self):
    super().__init__()
    self.require(Position)
    self.solid = False
