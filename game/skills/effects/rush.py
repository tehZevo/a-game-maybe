import game.components as C
from .skill_effect import SkillEffect

#rushing = moving in the facing direction
class Rush(SkillEffect):
  def __init__(self, force=1):
    super().__init__()
    self.force = force

  def start(self, skill):
    phys = skill.target.get_component(C.Physics)
    actor = skill.target.get_component(C.Actor)
    phys.apply_force(actor.move_dir * self.force)
