from actions import Action
from components import Physics, Stats
from utils import Vector

class Move(Action):
  def __init__(self, dir):
    super().__init__()
    self.interruptible = True
    self.dir = dir

  def update(self):
    from components import Actor
    #TODO: lol
    look_dir = Vector(0, 1) if self.dir.y > 0.5 else Vector(0, -1) if self.dir.y < -0.5 else Vector(1, 0) if self.dir.x > 0.5 else Vector(-1, 0) if self.dir.x < -0.5 else Vector()
    self.get_component(Actor).look_dir = look_dir
    phys = self.get_component(Physics)
    stats = self.get_component(Stats)
    force = self.dir.normalized() * stats.secondary_stats.move_speed * stats.move_speed_multiplier
    phys.apply_force(force)
