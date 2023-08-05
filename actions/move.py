from actions import Action
from components import Physics, Stats

class Move(Action):
  def __init__(self, dir):
    super().__init__()
    self.interruptible = True
    self.dir = dir

  def update(self):
    phys = self.get_component(Physics)
    stats = self.get_component(Stats)
    force = self.dir.normalized() * stats.move_speed
    phys.apply_force(force.x, force.y)
