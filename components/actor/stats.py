from ecs import Component
from stats import calculator

#TODO: solve circular dependencies by implementing equiplistener?
class Stats(Component):
  def __init__(self):
    super().__init__()
    #TODO: calculate
    self.hp = 1
    self.mp = 1
    self.move_speed_multiplier = 1
    self.primary_stats = self.equip_stats = self.secondary_stats = None

  def start(self):
    self.recalculate()
    self.hp = self.secondary_stats.hp
    self.mp = self.secondary_stats.mp

  def add_hp(self, hp):
    self.set_hp(self.hp + hp)

  def add_mp(self, mp):
    self.set_mp(self.mp + mp)

  def set_hp(self, hp):
    self.hp = max(0, min(hp, self.secondary_stats.hp))

  def set_mp(self, mp):
    self.mp = max(0, min(mp, self.secondary_stats.mp))

  def recalculate(self):
    self.primary_stats, self.equip_stats, self.secondary_stats = calculator.calculate(self.entity)
    self.hp = min(self.hp, self.secondary_stats.hp)
    self.mp = min(self.mp, self.secondary_stats.mp)
