import random

import game.components as C
from .skill_effect import SkillEffect
from game.constants import DAMAGE_SPREAD

class Heal(SkillEffect):
  def __init__(self, power=100):
    super().__init__()
    self.power = power

  def start(self, skill):
    user_stats = skill.user[C.Stats].stats.secondary
    #TODO: assumes heal is based on matt
    healing = user_stats.mag_att * self.power / 100.
    healing = healing * DAMAGE_SPREAD
    skill.target[C.Actor].heal(healing)