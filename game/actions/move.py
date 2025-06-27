import game.components as C
from game.utils import Vector
from . import Action

class Move(Action):
  def deserialize(action_data):
    dir = action_data["dir"]
    dir = dir and Vector(dir["x"], dir["y"]) 
    return Move(dir)

  def __init__(self, dir):
    super().__init__()
    self.interruptible = True
    self.dir = dir and dir.normalized()
    self.active = True
  
  def serialize(self):
    return {"dir": self.dir}

  def start(self):
    if self.dir is None or self.dir == Vector.ZERO:
      self.active = False
      return

  def update(self):
    if not self.active:
      return
    look_dir = Vector(0, 1) if self.dir.y > 0.5 else Vector(0, -1) if self.dir.y < -0.5 else Vector(1, 0) if self.dir.x > 0.5 else Vector(-1, 0) if self.dir.x < -0.5 else None
    if look_dir is not None:
      self.get_component(C.Actor).look_dir = look_dir
    self.get_component(C.Actor).move_dir = self.dir or Vector.ZERO
    phys = self.get_component(C.Physics)
    stats = self.get_component(C.Stats)
    force = self.dir.normalized() * stats.stats.secondary.move_speed * stats.move_speed_multiplier
    phys.apply_force(force)

    sprite = self.get_component(C.Sprite)
    sprite.set_animation("walk_down")