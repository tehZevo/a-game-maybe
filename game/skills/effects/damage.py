import random

import game.components as C
from .skill_effect import SkillEffect

class Damage(SkillEffect):
  def __init__(self, power=100):
    super().__init__()
    self.power = power

  def start(self, skill):
    if skill.target[C.Invulnerable] is not None:
      return

    user_stats = skill.user[C.Stats].stats.secondary
    target_stats = skill.target[C.Stats].stats.secondary
    crit_ratio = user_stats.critical / 100
    #determine crit
    is_crit = random.random() < crit_ratio
    crit_damage_rate = 2 + max(crit_ratio - 1, 0) #TODO: confirm
    
    #calc damage
    damage = user_stats.phys_att * self.power / 100. - target_stats.phys_def
    if is_crit:
      damage = damage * crit_damage_rate
    #dont heal lol
    damage = max(damage, 0)
    skill.target[C.Actor].damage(damage, crit=is_crit)
