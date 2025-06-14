import game.components as C
from game.components.actor import Actor
from .skill_effect import SkillEffect

#rushing = moving in the facing direction
class Rush(SkillEffect):
  def __init__(self, force=1):
    super().__init__()
    self.target = None
    self.force = force

  def start(self):
    self.target.get_component(C.Physics).apply_force(self.target.get_component(Actor).look_dir * self.force)
