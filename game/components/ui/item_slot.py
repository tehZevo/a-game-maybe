import pygame

from ..physics import Position
from .ui_component import UIComponent
import game.components as C
from game.utils.image_cache import get_image
from game.items.slots import ArmorSlot, SkillSlot, WeaponSlot
from game.utils import Vector

class ItemSlot(UIComponent):
  def __init__(self, slot_type, slot):
    super().__init__()
    self.slot_type = slot_type
    self.slot = slot
    self.player = None

  def set_player(self, player):
    self.player = player

  def get_icon(self):
    equips = self.player.get_component(C.Equips)
    equips = equips.armor if self.slot_type == ArmorSlot \
      else equips.skills if self.slot_type == SkillSlot \
      else equips.weapons
      
    item = equips[self.slot]
    icon = item and get_image(item.icon)
    return icon
    
  def draw(self, renderer):
    if self.player is None:
      return
    
    pos = self.get_component(Position).pos #TODO: cache pos comp
    border = get_image("assets/border.png")
    renderer.draw(border, pos.copy())
    icon = self.get_icon() #TODO: it would be great if we could cache the icon too
    if icon is not None:
      renderer.draw(icon, pos + Vector(4, 4))
