from skilleffects import SkillEffect
from components.actor.actor import Actor
from components.actor.stats import Stats

class Damage(SkillEffect):
  def __init__(self, power=100):
    super().__init__()
    self.target = None
    self.power = power

  def start(self):
    #calc damage
    user_stats = self.user.get_component(Stats).secondary_stats
    target_stats = self.target.get_component(Stats).secondary_stats
    #TODO: assumes physical, add constructor param for phys/mag
    damage = user_stats.phys_att * self.power / 100. - target_stats.phys_def
    #dont heal lol
    damage = max(damage, 0)
    self.target.get_component(Actor).damage(damage)
