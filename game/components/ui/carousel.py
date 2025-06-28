import pygame

from .ui_component import UIComponent
import game.components as C

from game.utils import Vector
from game.components.core import KeyHandler
from game.utils import image_utils
from game.utils.image_cache import get_image

class Carousel(UIComponent, KeyHandler):
  def __init__(self, labels, selection=0, size=None, on_change=lambda: None):
    super().__init__()
    self.labels = labels
    self.selection = selection
    self.on_change = on_change
    self.size = size or max([len(text) for text in labels])
  
  def handle_keys(self, kbd):
    old_selection = self.selection
    if kbd.pressed[pygame.K_LEFT]:
      self.selection -= 1
    if kbd.pressed[pygame.K_RIGHT]:
      self.selection += 1
    self.selection %= len(self.labels)
    if old_selection != self.selection:
      self.on_change(self.selection)

  def draw(self, renderer):
    pos = self.entity[C.Position].pos
    left_arrow = get_image("assets/ui/arrow_left.png")
    right_arrow = get_image("assets/ui/arrow_right.png")

    renderer.draw(left_arrow, pos)

    selected_option_text = self.labels[self.selection]
    selected_option_text = selected_option_text[:self.size]
    image_utils.draw_text(renderer, selected_option_text, pos + Vector(8, 0), color=(255, 255, 255))

    renderer.draw(right_arrow, pos + Vector(8 + self.size * 8, 0))
