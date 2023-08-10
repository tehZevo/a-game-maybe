from dataclasses import dataclass
from enum import Enum

from utils.utils import dict_op

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
    return PrimaryStats(**dict_op(self.__dict__, other.__dict__, lambda a, b: a + b))
