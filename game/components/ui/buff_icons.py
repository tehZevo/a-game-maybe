import pygame

from ..physics import Position
from .ui_component import UIComponent
import game.components as C
from game.utils.image_cache import get_image
from game.items.slots import ArmorSlot, SkillSlot, WeaponSlot
from game.items.defs import Equip, SkillItem
from game.skills.skill_rank import skill_rank_icon
from game.items.equip_grade import equip_grade_icon
from game.items.rarity import Rarity, rarity_color

from game.utils import Vector, image_utils

class BuffIcons(UIComponent):
  def __init__(self):
    super().__init__()
    self.player = None

  def set_player(self, player):
    self.player = player
  
  def start(self):
    pos = self.get_component(Position)
    pos.pos = Vector(32, 32)

  def draw(self, renderer):
    if self.player is None:
      return
    
    #TODO: buff ordering? (sort?)
    buffs = self.player.get_component(C.Buffs).buffs.values()
    timer = get_image("assets/ui/buff_timer.png")
    
    for buff in buffs:
      #TODO: flash when time < 10s?
      if buff.buffdef.icon is None:
        continue
      
      buff_image = get_image(buff.buffdef.icon)
      t = buff.time / buff.initial_time
      timer_frame = image_utils.get_frame_t(timer, 8, 1 - t)
      renderer.draw(buff_image, pos.copy())
      renderer.draw(timer_frame, pos.copy(), None, (0, 0, 0), 0.5)
