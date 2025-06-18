from game.buffs import BuffEffect
import game.components as C

class ChildBuff(BuffEffect):
  def __init__(self, buffdef, power_scale=1):
    super().__init__()
    self.buffdef = buffdef
    self.power_scale = power_scale

  def apply(self, buff):
    buffs_comp = buff.target.get_component(C.Buffs)
    #apply buff and store whether we were successful
    power = buff.power * self.power_scale
    was_applied = buffs_comp.apply_buff(self.buffdef, power, buff.time, buff.caster)
    print(self.buffdef, was_applied, power)
    return was_applied

  def remove(self, buff, was_applied):
    if not was_applied:
      return
    buffs_comp = buff.target.get_component(C.Buffs)
    buffs_comp.remove_buff(self.buffdef)
