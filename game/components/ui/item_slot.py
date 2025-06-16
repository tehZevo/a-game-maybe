import pygame

from ..physics import Position
from .ui_component import UIComponent
import game.components as C
from game.utils.image_cache import get_image
from game.items.slots import ArmorSlot, SkillSlot, WeaponSlot
from game.items.defs import Equip, SkillItem
from game.skills.skill_rank import skill_rank_icon
from game.items.equip_grade import equip_grade_icon

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
      mini_icon = skill_rank_icon(item.rank)
      return mini_icon and get_image(mini_icon)
    return None

  def get_icons(self):
    equips = self.player.get_component(C.Equips)
    equips = equips.armor if self.slot_type == ArmorSlot \
      else equips.skills if self.slot_type == SkillSlot \
      else equips.weapons
    
    item = equips[self.slot]
    mini_icon = item and self.get_mini_icon(item)

    icon = item and get_image(item.icon)
    return icon, mini_icon
  
  def draw(self, renderer):
    if self.player is None:
      return
    
    pos = self.get_component(Position).pos #TODO: cache pos comp
    border = get_image("assets/border.png")
    small_border = get_image("assets/small_border.png")
    renderer.draw(border, pos.copy())
    icon, mini_icon = self.get_icons() #TODO: it would be great if we could cache the icon too
    if icon is not None:
      renderer.draw(icon, pos + Vector(4, 4))
    if mini_icon is not None:
      renderer.draw(small_border, pos + Vector(14, -2))
      renderer.draw(mini_icon, pos + Vector(16, 0))
