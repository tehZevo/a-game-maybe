from uuid import uuid4

import game.components as C
from game.buffs.buff_effect import BuffEffect

class ModifyStats(BuffEffect):
  def __init__(self, flat=None, scaling=None):
    super().__init__()
    self.flat = flat
    self.scaling = scaling
  
  def apply(self, buff):
    id = str(uuid4())
    stats = buff.target.get_component(C.Stats)
    if self.flat is not None:
      stats.add_flat_modifier(id, self.flat)
    if self.scaling is not None:
      stats.add_scaling_modifier(id, self.scaling)
    return id
  
  def remove(self, buff, id):
    stats = buff.target.get_component(C.Stats)
    if self.flat is not None:
      stats.remove_flat_modifier(id)
    if self.scaling is not None:
      stats.remove_scaling_modifer(id)