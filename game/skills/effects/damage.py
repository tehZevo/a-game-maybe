import game.components as C
from .skill_effect import SkillEffect

class Damage(SkillEffect):
  def __init__(self, power=100):
    super().__init__()
    self.power = power

  def start(self, skill):
    if skill.target[C.Invulnerable] is not None:
      return

    #calc damage
    user_stats = skill.user[C.Stats].stats.secondary
    target_stats = skill.target[C.Stats].stats.secondary
    damage = user_stats.phys_att * self.power / 100. - target_stats.phys_def
    #dont heal lol
    damage = max(damage, 0)
    skill.target.get_component(C.Actor).damage(damage)
