from dataclasses import dataclass
from enum import Enum

EquipStat = Enum("EquipStat", ["PATT", "MATT", "PDEF", "MDEF"])

@dataclass
class EquipStats:
  PATT: int = 0
  MATT: int = 0
  PDEF: int = 0
  MDEF: int = 0

  #make subscriptable
  def __getitem__(self, key):
    return super().__getattribute__(key)

  def __add__(self, other):
    return EquipStats(
      self.PATT + other.PATT,
      self.MATT + other.MATT,
      self.PDEF + other.PDEF,
      self.MDEF + other.MDEF,
    )
