from ecs import Component
from items import Armor, Skill
from items.slots import ArmorSlot, SkillSlot

NUM_WEAPONS = 2

class Equips(Component):
  def __init__(self):
    super().__init__()
    self.armor = {slot: None for slot in ArmorSlot}
    self.skills = {slot: None for slot in SkillSlot}
    self.weapons = {n: None for n in range(NUM_WEAPONS)}
    self.cur_weapon = 0

  #cycles through weapons
  def switch_weapon(self):
    self.cur_weapon += 1
    self.cur_weapon %= NUM_WEAPONS

  def get_current_weapon(self):
    return self.weapons[self.cur_weapon]

  def equip(self, item):
    if issubclass(type(item), Armor):
      cur_equip = self.armor[item.slot]
      self.armor[item.slot] = item
      return cur_equip
    if issubclass(type(item), Skill):
      cur_equip = self.skills[item.slot]
      self.skills[item.slot] = item
      return cur_equip
    raise ValueError(f"Cannot equip {item}")
