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
    self.pos = pos

  def draw(self, renderer):
    if self.player is None:
      return
    
    buffs = self.player.get_component(C.ClientBuffs)
    if buffs is None:
      return
    buffs = buffs.buffs
    #TODO: buff ordering? (sort? maybe a param on buffdef?)
    buffs = self.player.get_component(C.ClientBuffs).buffs
    timer = get_image("assets/ui/buff_timer.png")
    buff_bg = get_image("assets/ui/buff_bg.png")
    pos = self.pos.pos.copy()

    for i, buff in enumerate(buffs):
      #TODO: flash when time < 10s?
      if buff.buffdef.icon is None:
        continue

      offset = Vector(i * 9, 0)
      buff_image = get_image(buff.buffdef.icon)
      t = max(buff.time / buff.initial_time, 0)
      timer_frame = image_utils.get_frame_t(timer, 8, 1 - t, clamp=True)
      renderer.draw(buff_bg, pos + offset)
      renderer.draw(buff_image, pos + offset)
      renderer.draw(timer_frame, pos + offset, None, (0, 0, 0), 0.5)
