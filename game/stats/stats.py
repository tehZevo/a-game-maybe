from dataclasses import dataclass, field

from .equip_stats import EquipStats
from .primary_stats import PrimaryStats
from .secondary_stats import SecondaryStats

@dataclass
class Stats:
  equip: EquipStats = field(default_factory=lambda: EquipStats())
  primary: PrimaryStats = field(default_factory=lambda: PrimaryStats())
  secondary: SecondaryStats = field(default_factory=lambda: SecondaryStats())

  def __add__(self, other):
    return Stats(
      self.equip + other.equip,
      self.primary + other.primary,
      self.secondary + other.secondary
    )
  
  def __mul__(self, other):
    if isinstance(other, EquipStats):
      return Stats(
        self.equip * other.equip,
        self.primary * other.primary,
        self.secondary * other.secondary
      )
    return Stats(
        self.equip * other,
        self.primary * other,
        self.secondary * other
      )

#convenience
Stats.Equips = lambda **kwargs: Stats(equip=EquipStats(**kwargs))
Stats.Primary = lambda **kwargs: Stats(primary=PrimaryStats(**kwargs))
Stats.Secondary = lambda **kwargs: Stats(secondary=SecondaryStats(**kwargs))
Stats.One = Stats(EquipStats.One(), PrimaryStats.One, SecondaryStats.One)