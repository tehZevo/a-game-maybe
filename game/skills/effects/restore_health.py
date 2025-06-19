import game.components as C
from .skill_effect import SkillEffect

class RestoreHealth(SkillEffect):
  def __init__(self, percent=100):
    super().__init__()
    self.target = None
    self.percent = percent

  def start(self, skill):
    stats = skill.target.get_component(C.Stats)
    stats.add_hp_percent(self.percent)
