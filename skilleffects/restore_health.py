from skilleffects import SkillEffect
from components.actor.stats import Stats

class RestoreHealth(SkillEffect):
  def __init__(self, percent=100):
    super().__init__()
    self.target = None
    self.percent = percent

  def start(self):
    stats = self.target.get_component(Stats)
    stats.add_hp(stats.secondary_stats.hp * self.percent)
