from ecs import Component
from stats import calculator, PrimaryStats, SecondaryStats, EquipStats

class Stats(Component):
  def __init__(self):
    super().__init__()
    #TODO: calculate
    self.move_speed = 100
    self.hp = 100
    self.mp = 100
    self.primary_stats = self.equip_stats = self.secondary_stats = None
    #TODO: how to (re)calculate stats? upon equip?

  def start(self):
    self.primary_stats, self.equip_stats, self.secondary_stats = calculator.calculate(self.entity)
    print(self.primary_stats)
    print(self.equip_stats)
    print(self.secondary_stats)
