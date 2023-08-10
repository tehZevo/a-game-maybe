from items import Equip
from stats import PrimaryStat

class Weapon(Equip):
  def __init__(self):
    super().__init__()
    self.physical_primary_stat = PrimaryStat.STR
    self.physical_secondary_stat = PrimaryStat.DEX
    self.magical_primary_stat = PrimaryStat.INT
    self.magical_secondary_stat = PrimaryStat.WIS
