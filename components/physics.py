from ecs import Component
from components import Position

class Physics(Component):
  def __init__(self):
    super().__init__()
    self.require(Position)

  def update(self):
    print("hello from physics")
