from game.ecs import Component
import game.components.ui as UI
import game.components as C
from game.items.slots import ArmorSlot, SkillSlot, WeaponSlot
from game.utils import Vector

#TODO: we need to know how tall the screen is..
def slot_position(x, y):
  #TODO: hardcoded y.. need to "anchor" to bottom of screen
  return Vector(2 + x * (24 + 2), 16 * 11 - 10 - (y * (24 + 2)))

ITEM_SLOTS = {
  (ArmorSlot, ArmorSlot.HAT): slot_position(0, 0),
  (ArmorSlot, ArmorSlot.SUIT): slot_position(1, 0),
  (ArmorSlot, ArmorSlot.GLOVES): slot_position(2, 0),
  (ArmorSlot, ArmorSlot.SHOES): slot_position(3, 0),
  (ArmorSlot, ArmorSlot.ACCESSORY): slot_position(4, 0),
  (WeaponSlot, WeaponSlot.PRIMARY): slot_position(5, 0),
  (WeaponSlot, WeaponSlot.SECONDARY): slot_position(6, 0),
  (SkillSlot, SkillSlot.ALPHA): slot_position(0, 1),
  (SkillSlot, SkillSlot.BETA): slot_position(0, 2),
  (SkillSlot, SkillSlot.GAMMA): slot_position(0, 3),
  (SkillSlot, SkillSlot.DELTA): slot_position(0, 4),
  (SkillSlot, SkillSlot.OMEGA): slot_position(0, 5),

  # (SkillSlot, SkillSlot.ALPHA): slot_position(0, 0),
  # (SkillSlot, SkillSlot.BETA): slot_position(1, 0),
  # (SkillSlot, SkillSlot.GAMMA): slot_position(2, 0),
  # (SkillSlot, SkillSlot.DELTA): slot_position(3, 0),
  # (SkillSlot, SkillSlot.OMEGA): slot_position(4, 0),
}

class HUD(Component):
  def __init__(self):
    super().__init__()
    self.game_world = None
    self.item_slots = {}

  def start(self):
    self.health_bar = self.entity.world.create_entity([UI.HealthBar()])
    self.mana_bar = self.entity.world.create_entity([UI.ManaBar()])
    for (slot_type, slot), pos in ITEM_SLOTS.items():
      item_slot = self.entity.world.create_entity([UI.ItemSlot(slot_type, slot), C.Position(pos)])
      self.item_slots[(slot_type, slot)] = item_slot
    self.buff_icons = self.entity.world.create_entity([UI.BuffIcons()])
  
  def set_player(self, player):
    print("player set", player)
    self.health_bar.get_component(UI.HealthBar).set_player(player)
    self.mana_bar.get_component(UI.ManaBar).set_player(player)
    for (_, _), item_slot in self.item_slots.items():
      item_slot.get_component(UI.ItemSlot).set_player(player)
    self.buff_icons.get_component(UI.BuffIcons).set_player(player)
