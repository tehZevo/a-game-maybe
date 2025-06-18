from game.components.actor import Stats
from .skill_effect import SkillEffect

class RestoreMana(SkillEffect):
  def __init__(self, percent=100):
    super().__init__()
    self.target = None
    self.percent = percent

  def start(self):
    stats = self.target.get_component(Stats)
    stats.add_mp_percent(self.percent)
