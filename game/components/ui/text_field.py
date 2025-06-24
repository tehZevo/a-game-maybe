import pygame

from .ui_component import UIComponent
import game.components as C
from game.utils.image_cache import get_image

from game.utils import Vector
from game.components.core import KeyHandler
from game.utils import image_utils

class TextField(UIComponent, KeyHandler):
  def __init__(self, on_submit, text="", draw_length=10, max_length=None):
    super().__init__()
    self.on_submit = on_submit
    self.draw_length = draw_length
    self.max_length = max_length
    self.text = text
  
  def handle_keys(self, pressed, held, released, unicode_pressed):
    if pressed[pygame.K_BACKSPACE]:
      self.text = self.text[:-1]
    elif pressed[pygame.K_RETURN]:
      self.on_submit(self.text)
    #TODO: clean
    elif unicode_pressed is not None and not (held[pygame.K_RCTRL] or held[pygame.K_LCTRL]):
      self.text += unicode_pressed
      if self.max_length is not None:
        self.text = self.text[:self.max_length]
  
  def draw(self, renderer):
    pos = self.entity[C.Position].pos
    image_utils.draw_9patch(renderer, "assets/ui/box.png", pos, self.draw_length + 2, 3)
    snippet = self.text[-self.draw_length:] + "_"
    image_utils.draw_text(renderer, snippet, pos + Vector(8, 8))
