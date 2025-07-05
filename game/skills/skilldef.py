from game.constants import DEFAULT_SKILL_USE_TIME
from .skill_rank import SkillRank

#TODO: reimpl hp/mp cost and use time as skill effects
#a skill has hp/mp costs, a use time, and effects
#a skill item has an icon, an equip slot, and drop rate?

class SkillDef:
  def __init__(self, id, effects, is_attack=True, rank=None, cooldown=None,
    mp_cost=0, hp_cost=0, use_time=DEFAULT_SKILL_USE_TIME,
    slot=None, icon=None, mini_icon=None,
    weapon_filter=lambda primary, secondary: True):
    if not isinstance(effects, (list, tuple)):
      effects = [effects]
    self.cooldown = cooldown
    self.id = id
    self.effects = effects
    self.rank = rank or SkillRank.I
    self.mp_cost = mp_cost
    self.hp_cost = hp_cost
    self.use_time = use_time
    self.slot = slot
    self.icon = icon
    self.mini_icon = mini_icon
    self.is_attack = is_attack
