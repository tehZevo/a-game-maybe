from game.ecs import Component
from game.constants import DT

#become invulnerable for [time] seconds; None for forever
class Invulnerable(Component):
  def __init__(self, time):
    super().__init__()
    self.time = time

  def update(self):
    if self.time is None:
      return

    self.time -= DT
    if self.time <= 0:
      self.entity.remove_component(self)
