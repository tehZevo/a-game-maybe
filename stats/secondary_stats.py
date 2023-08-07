from dataclasses import dataclass

@dataclass
class SecondaryStats:
  hp: int = 0
  mp: int = 0
  phys_att: int = 0
  mag_att: int = 0
  phys_def: int = 0
  mag_def: int = 0
  accuracy: int = 0
  evasion: int = 0
  move_speed: int = 0

  #make subscriptable
  def __getitem__(self, key):
    return super().__getattribute__(key)

  def __add__(self, other):
    pass
    #TODO
