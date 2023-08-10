from actions import Action
from components.physics.physics import Physics
from components.actor.stats import Stats
from utils import Vector

class Move(Action):
  def __init__(self, dir):
    super().__init__()
    self.interruptible = True
    self.dir = dir

  def update(self):
    from components.actor.actor import Actor
    #TODO: lol
    #TODO: if we somehow move(0, 0), dont update look_dir
    look_dir = Vector(0, 1) if self.dir.y > 0.5 else Vector(0, -1) if self.dir.y < -0.5 else Vector(1, 0) if self.dir.x > 0.5 else Vector(-1, 0) if self.dir.x < -0.5 else None
    if look_dir is not None:
      self.get_component(Actor).look_dir = look_dir
    phys = self.get_component(Physics)
    stats = self.get_component(Stats)
    force = self.dir.normalized() * stats.secondary_stats.move_speed * stats.move_speed_multiplier
    phys.apply_force(force)
