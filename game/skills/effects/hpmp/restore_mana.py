import game.components as C
from ..skill_effect import SkillEffect

class RestoreMana(SkillEffect):
  def __init__(self, percent=100):
    super().__init__()
    self.target = None
    self.percent = percent

  def start(self, skill):
    stats = skill.user[C.Stats]
    current_mp = stats.mp
    max_mp = stats.stats.secondary.mp
    missing_mp = max(max_mp - current_mp, 0)
    amount_to_heal = min(missing_mp, max_mp * self.percent)
    if amount_to_heal > 0:
      skill.target[C.Actor].heal_mp(amount_to_heal)
