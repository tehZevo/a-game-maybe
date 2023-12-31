from . import Equip
from game.stats import PrimaryStat

class Weapon(Equip):
  def __init__(self, equip_stats=None, primary_stats=None, secondary_stats=None):
    super().__init__(equip_stats, primary_stats, secondary_stats)
    self.physical_primary_stat = PrimaryStat.STR
    self.physical_secondary_stat = PrimaryStat.DEX
    self.magical_primary_stat = PrimaryStat.INT
    self.magical_secondary_stat = PrimaryStat.WIS
