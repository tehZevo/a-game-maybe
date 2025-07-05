import game.components as C
from ..skill_effect import SkillEffect

#TODO: in order to calculate this correctly, we would have to chain this with the damage done
class StealHP(SkillEffect):
  def __init__(self, power=100):
    super().__init__()
    self.power = power

  def start(self, skill):
    if skill.target[C.Invulnerable] is not None:
      return

    #calc damage
    user_stats = skill.user[C.Stats].stats.secondary
    target_stats = skill.target[C.Stats]
    #TODO: assumes physical, add constructor param for phys/mag
    damage = user_stats.phys_att * self.power / 100. - target_stats.stats.secondary.phys_def
    damage = max(damage, 0)
    amount_to_heal = min(damage, target_stats.hp)
    skill.user[C.Actor].heal(amount_to_heal)
