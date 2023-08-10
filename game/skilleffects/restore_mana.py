from skilleffects import SkillEffect
from components.actor.stats import Stats

class RestoreMana(SkillEffect):
  def __init__(self, percent=100):
    super().__init__()
    self.target = None
    self.percent = percent

  def start(self):
    stats = self.target.get_component(Stats)
    stats.add_mp(stats.secondary_stats.mp * self.percent)
