import pygame

import game.components as C
from game.utils import Vector
from game.utils import image_utils
from ..screen import Screen

class StatsScreen(Screen):
  def __init__(self, player):
    super().__init__()
    self.player = player
    #TODO: meh
    self.ui_manager = None
  
  def on_destroy(self):
    self.ui_manager.pop()
  
  def handle_keys(self, kb):
    if kb.pressed[pygame.K_RETURN]:
      self.entity.remove()

  def draw(self, renderer):
    stats = self.player[C.Stats].stats
    e = stats.equip
    p = stats.primary
    s = stats.secondary

    left_lines = [
      "Equip:",
      f"PATT: {e.PATT}",
      f"MATT: {e.MATT}",
      f"PDEF: {e.PDEF}",
      f"MDEF: {e.MDEF}",
      "",
      "Primary:",
      f"STR: {p.STR}",
      f"VIT: {p.VIT}",
      f"DEX: {p.DEX}",
      f"AGI: {p.AGI}",
      f"INT: {p.INT}",
      f"WIS: {p.WIS}",
    ]

    right_lines = [
      "Secondary:",
      f"HP: {s.hp}",
      f"MP: {s.mp}",
      f"Phys. Att.: {s.phys_att}",
      f"Mag. Att.: {s.mag_att}",
      f"Phys. Def.: {s.phys_def}",
      f"Mag. Def.: {s.mag_def}",
      f"Acc.: {s.accuracy}",
      f"Eva.: {s.evasion}",
      f"Move Spd: {s.move_speed}",
      f"Crit: {s.critical}",
    ]
    
    image_utils.draw_text_lines(renderer, left_lines, Vector(32, 32), color=(255, 255, 255))
    image_utils.draw_text_lines(renderer, right_lines, Vector(32 + 64 + 16, 32), color=(255, 255, 255))
