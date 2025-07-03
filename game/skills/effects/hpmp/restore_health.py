import game.components as C
from ..skill_effect import SkillEffect

class RestoreHealth(SkillEffect):
  def __init__(self, percent=100):
    super().__init__()
    self.target = None
    self.percent = percent

  def start(self, skill):
    stats = skill.user[C.Stats]
    current_hp = stats.hp
    max_hp = stats.stats.secondary.hp
    missing_hp = max(max_hp - current_hp, 0)
    amount_to_heal = min(missing_hp, max_hp * self.percent)
    if amount_to_heal > 0:
      skill.target[C.Actor].heal(amount_to_heal)
