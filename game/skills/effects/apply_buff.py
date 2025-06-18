from game.buffs import Buff
from .skill_effect import SkillEffect
import game.components as C

#TODO: stacks?

no_scaling = lambda stats: 0

class ApplyBuff(SkillEffect):
  def __init__(self, buffdef, flat_power=0, flat_time=0, power_scaling=no_scaling, time_scaling=no_scaling):
    super().__init__()
    self.buffdef = buffdef
    self.flat_power = flat_power
    self.flat_time = flat_time
    self.power_scaling = power_scaling
    self.time_scaling = time_scaling

  def start(self):
    stats = self.target.get_component(C.Stats).stats
    buffs = self.target.get_component(C.Buffs)
    #calc power/time
    power = self.flat_power + self.power_scaling(stats)
    time = self.flat_time + self.time_scaling(stats)
    #create and apply instance
    buffs.apply_buff(self.buffdef, power, time, self.user)
