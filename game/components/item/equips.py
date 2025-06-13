from game.ecs import Component
from game.items.hierarchy import Armor, SkillItem
from game.items.slots import ArmorSlot, SkillSlot
from ..core.savable import Savable
import game.components as C

NUM_WEAPONS = 2

#TODO: separate skills from equips?
# maybe monsters shouldnt have skills in "slots", but should still "wear" equips (to better control their stats)
# that or have monster archetypes that just have stats...
class Equips(Component, Savable):
  def __init__(self):
    super().__init__()
    self.require(C.Stats)
    self.armor = {slot: None for slot in ArmorSlot}
    self.skills = {slot: None for slot in SkillSlot}
    self.weapons = {n: None for n in range(NUM_WEAPONS)}
    self.cur_weapon = 0

  def alert_listeners(self):
    for listener in self.entity.find(C.EquipsListener):
      listener.on_equips_changed(self)

  #cycles through weapons
  def switch_weapon(self):
    self.cur_weapon += 1
    self.cur_weapon %= NUM_WEAPONS
    self.alert_listeners()
    self.get_component(C.Stats).recalculate()

  def get_current_weapon(self):
    return self.weapons[self.cur_weapon]

  def equip(self, item):
    #TODO: equipping weapons

    if issubclass(type(item), Armor):
      cur_equip = self.armor[item.armor_slot]
      self.armor[item.armor_slot] = item
      self.alert_listeners()
      self.get_component(C.Stats).recalculate()
      return cur_equip

    if issubclass(type(item), SkillItem):
      cur_equip = self.skills[item.skilldef.slot]
      self.skills[item.skilldef.slot] = item
      self.alert_listeners()
      self.get_component(C.Stats).recalculate()
      return cur_equip

    raise ValueError(f"Cannot equip {item}")

  def save_keys(self):
    return ["armor", "skills", "weapons", "cur_weapon"]
