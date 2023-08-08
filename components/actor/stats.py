from ecs import Component

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

  def recalculate(self):
    self.primary_stats, self.equip_stats, self.secondary_stats = calculator.calculate(self.entity)
    self.hp = min(self.hp, self.secondary_stats.hp)
    self.mp = min(self.mp, self.secondary_stats.mp)

#TODO: reee
from stats import calculator
