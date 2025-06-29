import game.components as C
from .skill_effect import SkillEffect

class Heal(SkillEffect):
  def __init__(self, power=100):
    super().__init__()
    self.power = power

  def start(self, skill):
    user_stats = skill.user[C.Stats].stats.secondary
    #TODO: assumes heal is based on matt
    healing = user_stats.mag_att * self.power / 100.
    print(user_stats.mag_att)
    skill.target[C.Actor].heal(healing)