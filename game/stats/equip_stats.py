from dataclasses import dataclass, field
from enum import IntEnum
from typing import ClassVar

from game.utils.utils import dict_op

EquipStat = IntEnum("EquipStat", ["PATT", "MATT", "PDEF", "MDEF"])

@dataclass
class EquipStats:
  PATT: int = 0
  MATT: int = 0
  PDEF: int = 0
  MDEF: int = 0

  #TODO: remove, unneeded
  @classmethod
  def One(cls): return EquipStats(1, 1, 1, 1)

  #make subscriptable
  def __getitem__(self, key):
    return super().__getattribute__(key)

  def __add__(self, other):
    return EquipStats(**dict_op(self.__dict__, other.__dict__, lambda a, b: a + b))

  def __mul__(self, other):
    if isinstance(other, EquipStats):
      return EquipStats(**dict_op(self.__dict__, other.__dict__, lambda a, b: a * b))
    return EquipStats(**{k: v * other for k, v in self.__dict__.items()})

  def as_ints(self):
    return EquipStats(**{k: int(v) for k, v in self.__dict__.items()})