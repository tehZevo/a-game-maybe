import pygame

import game.components as C
from game.utils.image_cache import get_image
from game.items.slots import ArmorSlot, SkillSlot, WeaponSlot
from game.items.defs import Equip, SkillItem
from game.skills.skill_rank import skill_rank_icon
from game.items.equip_grade import equip_grade_icon
from game.items.rarity import Rarity, rarity_color
from ..ui_component import UIComponent

from game.utils import Vector
class ItemSlot(UIComponent):
  def __init__(self, slot_type, slot):
    super().__init__()
    self.slot_type = slot_type
    self.slot = slot
    self.player = None

  def set_player(self, player):
    self.player = player
  
  def get_mini_icon(self, item):
    if isinstance(item, Equip):
      mini_icon = equip_grade_icon(item.grade)
      return mini_icon and get_image(mini_icon)
    if isinstance(item, SkillItem):
      mini_icon = skill_rank_icon(item.skilldef.rank)
      return mini_icon and get_image(mini_icon)
    return None

  def get_item(self):
    equips = self.player.get_component(C.Equips)
    equips = equips.armor if self.slot_type == ArmorSlot \
      else equips.skills if self.slot_type == SkillSlot \
      else equips.weapons
    
    return equips[self.slot]
  
  def draw(self, renderer):
    if self.player is None:
      return
    
    pos = self.get_component(C.Position).pos #TODO: cache pos comp
    slot_bg = get_image("assets/ui/slot_bg.png")
    slot_border = get_image("assets/ui/slot_border.png")
    rank_bg = get_image("assets/ui/rank_bg.png")
    rank_border = get_image("assets/ui/rank_border.png")
    
    renderer.draw(slot_bg, pos.copy())
    #TODO: it would be great if we could cache this stuff too
    item = self.get_item()
    icon = item and get_image(item.icon)
    mini_icon = item and self.get_mini_icon(item)
    #TODO: naming
    other_mini_icon = item and item.mini_icon and get_image(item.mini_icon)
    rarity = item and item.rarity or Rarity.COMMON
    border_color = rarity and rarity_color(rarity)

    renderer.draw(slot_bg, pos.copy())
    renderer.draw(slot_border, pos.copy(), tint=border_color)
    if icon is not None:
      renderer.draw(icon, pos + Vector(4, 4))
    if mini_icon is not None:
      renderer.draw(rank_bg, pos + Vector(14, -2))
      renderer.draw(rank_border, pos + Vector(14, -2), tint=border_color)
      renderer.draw(mini_icon, pos + Vector(16, 0), tint=border_color)
    if other_mini_icon is not None:
      renderer.draw(other_mini_icon, pos + Vector(4, 12), alpha=0.8)
