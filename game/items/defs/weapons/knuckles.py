from .weapon import Weapon
from game.items.weapon_type import WeaponType

class Knuckles(Weapon):
  def __init__(self, **kwargs):
    super().__init__(weapon_type=WeaponType.KNUCKLES, **kwargs)
