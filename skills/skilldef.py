
DEFAULT_USE_TIME = 0.5 #seconds

#TODO: could hp/mp cost and use time be impl'd as skill effects?

#a skill has hp/mp costs, a use time, and effects
#a skill item has an icon, an equip slot, and drop rate?

class SkillDef:
  def __init__(self, effects, mp_cost=0, hp_cost=0, use_time=DEFAULT_USE_TIME, slot=None, icon=None):
    self.effects = effects
    self.mp_cost = mp_cost
    self.hp_cost = hp_cost
    self.use_time = use_time
    self.slot = slot
    self.icon = icon
