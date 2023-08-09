from ecs import Component
from components.physics.rect import Rect

#just a flag component for physics
class Collisions(Component):
  def __init__(self):
    super().__init__()
    self.require(Rect)
