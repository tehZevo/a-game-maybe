from game.ecs import Component
import game.components as C
from game.buffs import Buff

#TODO: BuffsSyncing
class Buffs(Component):
  def __init__(self):
    super().__init__()
    self.buffs = {}

  def should_apply(self, existing, power, time):
    return existing is None \
      or power > existing.power \
      or (power == existing.power and time > existing.time)
  
  def get_buff(self, buffdef):
    return self.buffs.get(buffdef.__class__)

  def apply_buff(self, buffdef, power, time, caster):
    """Returns true if buff was applied"""
    buff_type = buffdef.__class__
    existing = self.buffs.get(buff_type)
    
    if not self.should_apply(existing, power, time):
      return False
    
    buff = Buff(buffdef, power, time, self.entity, caster)
    existing and existing.remove()
    self.buffs[buff_type] = buff
    buff.apply()
    
    return True
  
  def remove_buff(self, buffdef):
    existing = self.get_buff(buffdef)
    if existing is not None:
      existing.remove()
      del self.buffs[buffdef.__class__]
    
  def update(self):
    for buff in self.buffs.values():
      if buff.time <= 0:
        buff.remove()
        continue
      buff.update()
    
    self.buffs = {k: v for k, v in self.buffs.items() if v.time > 0}
