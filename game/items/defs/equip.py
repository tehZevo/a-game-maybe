from game.stats import EquipStats, PrimaryStats, SecondaryStats
from .itemdef import ItemDef
from game.items.equip_grade import EquipGrade

class Equip(ItemDef):
  def __init__(self, grade=None, equip_stats=None, primary_stats=None, secondary_stats=None, **kwargs):
    super().__init__(**kwargs)
    self.grade = grade or EquipGrade.UNKNOWN
    self.equip_stats = equip_stats or EquipStats()
    self.primary_stats = primary_stats or PrimaryStats()
    self.secondary_stats = secondary_stats or SecondaryStats()
