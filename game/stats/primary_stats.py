from dataclasses import dataclass
from enum import IntEnum

from game.utils.utils import dict_op

PrimaryStat = IntEnum("PrimaryStat", ["STR", "VIT", "DEX", "AGI", "INT", "WIS"])

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
    return PrimaryStats(**dict_op(self.__dict__, other.__dict__, lambda a, b: a + b))

  def __mul__(self, other):
    if isinstance(other, PrimaryStats):
      return PrimaryStats(**dict_op(self.__dict__, other.__dict__, lambda a, b: int(a * b)))
    return PrimaryStats(**{k: int(v * other) for k, v in self.__dict__.items()})

PrimaryStats.One = PrimaryStats(1, 1, 1, 1, 1, 1)
PrimaryStats.Str = PrimaryStats(STR=1)
PrimaryStats.Vit = PrimaryStats(VIT=1)
PrimaryStats.Dex = PrimaryStats(DEX=1)
PrimaryStats.Agi = PrimaryStats(AGI=1)
PrimaryStats.Int = PrimaryStats(INT=1)
PrimaryStats.Wis = PrimaryStats(WIS=1)

