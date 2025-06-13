from .weapon import Weapon
from game.items.weapon_type import WeaponType

class DaggerL(Weapon):
  def __init__(self, **kwargs):
    super().__init__(weapon_type=WeaponType.DAGGER_L, **kwargs)
