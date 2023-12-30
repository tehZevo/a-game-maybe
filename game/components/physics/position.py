from game.ecs import Component
from game.utils import Vector

class Position(Component):
  def __init__(self, pos=None):
    super().__init__()
    self.pos = Vector() if pos is None else pos
