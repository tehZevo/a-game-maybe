
DEFAULT_USE_TIME = 0.5 #seconds
#TODO: add cast time?
#TODO: could these be impl'd as skill effects?

class SkillDef:
  def __init__(self, effects, mp_cost=0, hp_cost=0, use_time=DEFAULT_USE_TIME):
    self.effects = effects
    self.mp_cost = mp_cost
    self.hp_cost = hp_cost
    self.use_time = use_time
