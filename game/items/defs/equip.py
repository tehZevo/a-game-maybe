from game.stats import EquipStats, PrimaryStats, SecondaryStats
from .itemdef import Itemdef

class Equip(Itemdef):
  def __init__(self, equip_stats=None, primary_stats=None, secondary_stats=None, **kwargs):
    super().__init__(**kwargs)
    self.equip_stats = equip_stats or EquipStats()
    self.primary_stats = primary_stats or PrimaryStats()
    self.secondary_stats = secondary_stats or SecondaryStats()
