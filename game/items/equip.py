from items import Item
from stats import EquipStats, PrimaryStats, SecondaryStats

class Equip(Item):
  def __init__(self):
    super().__init__()
    self.equip_stats = EquipStats()
    self.primary_stats = PrimaryStats()
    self.secondary_stats = SecondaryStats()
