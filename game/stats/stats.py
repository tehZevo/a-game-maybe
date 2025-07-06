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
  
  def as_ints(self):
    return Stats(
      self.equip.as_ints(),
      self.primary.as_ints(),
      self.secondary.as_ints()
    )

#convenience
Stats.Equip = lambda *args, **kwargs: Stats(equip=EquipStats(*args, **kwargs))
Stats.Primary = lambda *args, **kwargs: Stats(primary=PrimaryStats(*args, **kwargs))
Stats.Secondary = lambda *args, **kwargs: Stats(secondary=SecondaryStats(*args, **kwargs))
Stats.One = Stats(EquipStats.One(), PrimaryStats.One, SecondaryStats.One)