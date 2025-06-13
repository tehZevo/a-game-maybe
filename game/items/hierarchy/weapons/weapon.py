from ..equip import Equip
from game.items.weapon_type import WeaponType, weapon_slot

class Weapon(Equip):
  def __init__(self, weapon_type=None, **kwargs):
    super().__init__(**kwargs)
    self.weapon_type = weapon_type
    self.weapon_slot = weapon_slot(weapon_type)