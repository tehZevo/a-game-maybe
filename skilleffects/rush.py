from skilleffects import SkillEffect
from components import Position, Physics, Actor

#rushing = moving in the facing direction
class Rush(SkillEffect):
  def __init__(self, force=1):
    super().__init__()
    self.target = None
    self.force = force

  def start(self):
    self.target.get_component(Physics).apply_force(self.target.get_component(Actor).look_dir * self.force)
