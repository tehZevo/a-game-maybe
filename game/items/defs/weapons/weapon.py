from ..equip import Equip
from game.items.weapon_type import WeaponType, weapon_slot, default_weapon_primary_archetype, default_weapon_equip_archetype

class Weapon(Equip):
  def __init__(self, weapon_type=None, primary_archetype=None, equip_archetype=None, \
    attack_skill=None, charge_skill=None, **kwargs
  ):
    primary_archetype = primary_archetype or default_weapon_primary_archetype(weapon_type)
    equip_archetype = equip_archetype or default_weapon_equip_archetype(weapon_type)
    super().__init__(primary_archetype=primary_archetype, equip_archetype=equip_archetype, **kwargs)
    self.weapon_type = weapon_type
    self.attack_skill = attack_skill
    #TODO
    self.charge_skill = charge_skill
    self.weapon_slot = weapon_slot(weapon_type)