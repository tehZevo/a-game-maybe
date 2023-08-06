from enum import Enum

from ecs import Component

EquipmentSlot = Enum("EquipmentSlot", ["HAT", "ARMOR", "GLOVES", "SHOES", "ACCESSORY"])

class Equipment(Component):
  def __init__(self):
    super().__init__()
    self.equips = {slot: None for slot in EquipmentSlot}

  def get_equip(self, slot):
    if type(slot) != type(EquipmentSlot.HAT):
      raise ValueError(f"{slot} is not a member of {EquipmentSlot}")
    return self.equips[slot]

  #returns current equip in slot
  def set_equip(self, slot, equip):
    #TODO: check that equip is equip type? or has equip component?
    #TODO: or is equip game data?
    if type(slot) != type(EquipmentSlot.HAT):
      raise ValueError(f"{slot} is not a member of {EquipmentSlot}")
    cur_equip = self.get_equip(slot)
    print(f"equipping {equip} to {slot}")
    self.equips[slot] = equip
    return cur_equip
