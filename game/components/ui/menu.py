import pygame

from .ui_component import UIComponent
import game.components as C

from game.utils import Vector
from game.components.core import KeyHandler
from game.utils import image_utils

class Menu(UIComponent, KeyHandler):
  def __init__(self, options=[], selection=0):
    super().__init__()
    self.options = options
    self.selection = 0
    self.max_option_length = max([len(text) for text, _ in self.options])
    self.ui_manager = None
  
  def on_destroy(self):
    self.ui_manager.pop()
    
  def handle_keys(self, kbd):
    if kbd.pressed[pygame.K_DOWN]:
      self.down()
    if kbd.pressed[pygame.K_UP]:
      self.up()
    if kbd.pressed[pygame.K_SPACE]:
      self.select()
  
  def down(self):
    self.selection = max(0, min(self.selection + 1, len(self.options) - 1))
  
  def up(self):
    self.selection = max(0, min(self.selection - 1, len(self.options) - 1))
  
  def select(self):
    self.options[self.selection][1](self)
  
  def draw(self, renderer):
    pos = self.get_component(C.Position).pos #TODO: cache pos comp
    max_len = max([len(o) for o in self.options])
    image_utils.draw_9patch(renderer, "assets/ui/box.png", pos, self.max_option_length + 2 + 1, len(self.options) + 2)
    for i, (text, _) in enumerate(self.options):
      spacer = ">" if i == self.selection else " "
      image_utils.draw_text(renderer, spacer + text, pos + Vector(8, (i + 1) * 8))