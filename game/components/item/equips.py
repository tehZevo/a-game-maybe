from game.ecs import Component
from game.items.defs import Armor, SkillItem, Weapon
from game.items.slots import ArmorSlot, SkillSlot, WeaponSlot
from ..core.savable import Savable
import game.components as C

#TODO: separate skills from equips?
# maybe monsters shouldnt have skills in "slots", but should still "wear" equips (to better control their stats)
# that or have monster archetypes that just have stats...
class Equips(Component, Savable):
  def __init__(self):
    super().__init__()
    self.require(C.Stats)
    self.armor = {slot: None for slot in ArmorSlot}
    self.skills = {slot: None for slot in SkillSlot}
    self.weapons = {slot: None for slot in WeaponSlot}

  def alert_listeners(self):
    for listener in self.entity.find(C.EquipsListener):
      listener.on_equips_changed(self)

  def equip(self, item):
    cur_equip = None
    if issubclass(type(item), Weapon):
      #TODO: handle dropping other weapon based on pairing logic
      cur_equip = self.weapons[item.weapon_slot]
      self.weapons[item.weapon_slot] = item

    if issubclass(type(item), Armor):
      cur_equip = self.armor[item.armor_slot]
      self.armor[item.armor_slot] = item

    if issubclass(type(item), SkillItem):
      cur_equip = self.skills[item.skilldef.slot]
      self.skills[item.skilldef.slot] = item

    self.alert_listeners()
    #TODO: make stats listen to equips?
    self.entity[C.Stats].recalculate()
    
    return cur_equip

  def save_keys(self):
    return ["armor", "skills", "weapons"]
