from ..equip import Equip
from game.items.weapon_type import WeaponType, weapon_slot

class Weapon(Equip):
  def __init__(self, weapon_type=None, attack_skill=None, **kwargs):
    super().__init__(**kwargs)
    self.weapon_type = weapon_type
    self.attack_skill = attack_skill
    self.weapon_slot = weapon_slot(weapon_type)