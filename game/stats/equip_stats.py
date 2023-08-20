from dataclasses import dataclass
from enum import IntEnum

from game.utils.utils import dict_op

EquipStat = IntEnum("EquipStat", ["PATT", "MATT", "PDEF", "MDEF"])

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
    return EquipStats(**dict_op(self.__dict__, other.__dict__, lambda a, b: a + b))
