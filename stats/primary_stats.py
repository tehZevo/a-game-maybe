from dataclasses import dataclass
from enum import Enum

PrimaryStat = Enum("PrimaryStat", ["STR", "VIT", "DEX", "AGI", "INT", "WIS"])

@dataclass
class PrimaryStats:
  STR: int = 0
  VIT: int = 0
  DEX: int = 0
  AGI: int = 0
  INT: int = 0
  WIS: int = 0

  #make subscriptable
  def __getitem__(self, key):
    return super().__getattribute__(key)

  def __add__(self, other):
    return PrimaryStats(
      self.STR + other.STR,
      self.VIT + other.VIT,
      self.DEX + other.DEX,
      self.AGI + other.AGI,
      self.INT + other.INT,
      self.WIS + other.WIS,
    )
