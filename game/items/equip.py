from game.stats import EquipStats, PrimaryStats, SecondaryStats
from . import Item

class Equip(Item):
  def __init__(self, equip_stats=None, primary_stats=None, secondary_stats=None):
    super().__init__()
    self.equip_stats = EquipStats() if equip_stats is None else equip_stats
    self.primary_stats = PrimaryStats() if primary_stats is None else primary_stats
    self.secondary_stats = SecondaryStats() if secondary_stats is None else secondary_stats
