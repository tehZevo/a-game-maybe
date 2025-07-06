from game.stats import Stats, PrimaryStats, EquipStats
from .itemdef import ItemDef
from game.items.equip_grade import EquipGrade

class Equip(ItemDef):
  def __init__(self, grade=None, primary_archetype=None, equip_archetype=None, \
    bonus_stats=None, **kwargs
  ):
    super().__init__(**kwargs)
    import game.stats.equip_stats_calculator as EC
    self.grade = grade or EquipGrade.UNKNOWN
    primary_archetype = primary_archetype or PrimaryStats()
    equip_archetype = equip_archetype or EquipStats()
    bonus_stats = bonus_stats or Stats()
    calced = EC.calc_primary_archetype_stats(primary_archetype, self.__class__, self.grade)
    #TODO: equip_archetype
    self.stats = calced + bonus_stats
