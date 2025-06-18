from game.ecs import Component
import game.components as C
from game.buffs import Buff

class Buffs(Component):
  def __init__(self):
    super().__init__()
    self.buffs = {}
    self.dirty = False

  def alert_listeners(self):
    for listener in self.entity.find(C.BuffsListener):
      listener.on_buffs_changed(self.buffs)

  def should_apply(self, existing, power, time):
    return existing is None \
      or power > existing.power \
      or (power == existing.power and time > existing.time)
  
  def get_buff(self, buffdef):
    return self.buffs.get(buffdef)

  def apply_buff(self, buffdef, power, time, caster):
    """Returns true if buff was applied"""
    existing = self.buffs.get(buffdef)
    
    if not self.should_apply(existing, power, time):
      return False
    
    buff = Buff(buffdef, power, time, self.entity, caster)
    existing and existing.remove()
    self.buffs[buffdef] = buff
    buff.apply()
    self.dirty = True
    
    return True
  
  def remove_buff(self, buffdef):
    existing = self.get_buff(buffdef)
    if existing is not None:
      existing.remove()
      del self.buffs[buffdef]
      self.dirty = True
    
  def update(self):
    for buff in list(self.buffs.values()):
      print("updating", buff.buffdef.id)
      buff.update()
      if buff.time <= 0:
        buff.remove()
        print("[Server] Buff expired:", buff.buffdef.id)
        self.dirty = True
        continue
    
    self.buffs = {k: v for k, v in self.buffs.items() if v.time > 0}

    if self.dirty:
      self.alert_listeners()
      self.dirty = False
      
