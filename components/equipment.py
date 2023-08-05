from enum import Enum
from collections import defaultdict

from ecs import Component

EquipmentSlot = EquipmentSlot("EquipmentSlot", ["HAT", "ARMOR", "GLOVES", "SHOES", "ACCESSORY"])

class Equipment(Component):
  def __init__(self):
    super().__init__()
    self.equips = defaultdict

  def get_equip(self, slot):
    if type(slot) != type(e.A):
      raise ValueError(f"{slot} is not a member of {EquipmentSlot})
    return self.equips[slot]

  #returns current equip in slot
  def set_equip(self, slot, equip):
    #TODO: check that equip is equip type? or has equip component?
    #TODO: or is equip game data?
    if type(slot) != type(e.A):
      raise ValueError(f"{slot} is not a member of {EquipmentSlot})
    cur_equip = self.get_equip(slot)
    self.equips[slot] = equip
